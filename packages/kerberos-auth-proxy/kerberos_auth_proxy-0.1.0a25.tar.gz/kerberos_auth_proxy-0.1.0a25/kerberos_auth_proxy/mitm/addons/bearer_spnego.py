from logging import getLogger
import os
import ssl
from typing import Optional
from urllib.parse import urlparse, ParseResult

import aiohttp
from mitmproxy.http import HTTPFlow
from timelength import TimeLength

from kerberos_auth_proxy.kerberos import KerberosCache
from kerberos_auth_proxy.mitm.hostutils import UrlPattern
from kerberos_auth_proxy.mitm.username import get_username

from kerberos_auth_proxy.mitm.addons.spnego import generate_spnego_negotiate
from kerberos_auth_proxy.utils import ExpiringCache

LOGGER = getLogger(__name__)


class BearerSpnegoAddon:
    def __init__(
        self,
        url_patterns: list[UrlPattern],
        token_url_format: str,
        token_method: Optional[str] = None,
        token_headers: Optional[dict[str, str]] = None,
        expiration: Optional[float] = None,
        default_username: Optional[str] = None,
    ) -> None:
        self.url_patterns = url_patterns
        self.token_url_format = token_url_format
        self.token_method = token_method or 'POST'
        self.token_headers = token_headers or {}
        self.expiration = expiration or 10*60
        self.kerberos_cache = KerberosCache()
        self.token_cache = ExpiringCache[str](
            init=self._get_token,
            expiration=expiration or 10*60,
        )
        self.default_username = default_username or None

    async def _get_token(self, user: str) -> str:
        username, _, netloc = user.partition('@')
        token_url = self.token_url_format % {'netloc': netloc}

        return await generate_bearer_spnego_token(
            cache=self.kerberos_cache,
            username=username,
            token_url=token_url,
            token_method=self.token_method,
            token_headers=self.token_headers,
        )

    @classmethod
    def create(
        cls,
        urls: list[str],
        token_url_format: str,
        token_method: Optional[str] = None,
        token_headers: Optional[dict[str, str]] = None,
        expiration: Optional[str] = None,
        default_username: Optional[str] = None,
    ) -> 'BearerSpnegoAddon':
        return cls(
            url_patterns=[UrlPattern.create(url) for url in (urls or [])],
            token_url_format=token_url_format,
            token_method=token_method,
            token_headers=token_headers,
            expiration=TimeLength(expiration).total_seconds if expiration else None,
            default_username=default_username or None,
        )

    async def request(self, flow: HTTPFlow):
        if not (username := get_username(flow, self.default_username)):
            LOGGER.debug('skipping Bearer SPNEGO flow, no valid username')
            return

        flow_url: ParseResult = urlparse(flow.request.url)
        if not UrlPattern.matches_any(self.url_patterns, flow_url):
            LOGGER.debug('skipping Bearer SPNEGO flow, URL does not match: %s', flow.request.url)
            return

        token, _ = await self.token_cache.get(username + "@" + (flow_url.netloc or ''))
        if token:
            flow.request.headers[b'Authorization'] = f'Bearer {token}'


async def generate_bearer_spnego_token(
    cache: KerberosCache,
    username: str,
    token_url: str,
    token_method: str,
    token_headers: Optional[dict[str, str]] = None,
) -> Optional[str]:
    token_headers = token_headers or {}
    authority = urlparse(token_url).netloc
    negotiate = await generate_spnego_negotiate(
        cache=cache,
        username=username,
        authority=authority,
    )
    headers = {**token_headers, 'Authorization': negotiate}

    LOGGER.info('generating Bearer SPNEGO token from %s %s', token_method, token_url)

    cafile = os.environ['MITM_SET_SSL_VERIFY_UPSTREAM_TRUSTED_CA']
    ciphers = os.getenv('SSL_CONTEXT_CIPHERS') or ''
    ssl_context = ssl.create_default_context(cafile=cafile)
    if ciphers:
        ssl_context.set_ciphers(ciphers)
    connector = aiohttp.TCPConnector(ssl=ssl_context)

    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.request(method=token_method, url=token_url, headers=headers) as response:
            if response.ok:
                return await response.text()
            else:
                LOGGER.warning('request failed with status=%d: %r', response.status, await response.text())
