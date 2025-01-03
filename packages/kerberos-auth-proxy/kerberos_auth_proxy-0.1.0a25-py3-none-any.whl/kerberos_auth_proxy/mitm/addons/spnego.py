import asyncio
from logging import getLogger
from typing import Optional
from urllib.parse import urlparse

import gssapi
from requests_gssapi import HTTPSPNEGOAuth
from mitmproxy.http import HTTPFlow

from kerberos_auth_proxy.kerberos import KerberosCache
from kerberos_auth_proxy.mitm.hostutils import UrlPattern
from kerberos_auth_proxy.mitm.username import get_username

LOGGER = getLogger(__name__)


class SpnegoAddon:
    def __init__(
        self,
        url_patterns: list[UrlPattern],
        default_username: Optional[str] = None,
    ) -> None:
        self.url_patterns = url_patterns
        self.default_username = default_username or None
        self.cache = KerberosCache()

    @classmethod
    def create(
        cls,
        urls: Optional[list[str]] = None, 
        default_username: Optional[str] = None,
    ) -> 'SpnegoAddon':
        return cls(
            url_patterns=[UrlPattern.create(url) for url in (urls or [])],
            default_username=default_username or None,
        )

    async def request(self, flow: HTTPFlow):
        if not (username := get_username(flow, self.default_username)):
            LOGGER.debug('skipping SPNEGO flow, no valid username')
            return

        flow_url = urlparse(flow.request.url)
        if not UrlPattern.matches_any(self.url_patterns, flow_url):
            LOGGER.debug('skipping SPNEGO flow, URL does not match: %s', flow.request.url)
            return

        negotiate = await generate_spnego_negotiate(
            cache=self.cache,
            authority=flow.request.host,
            username=username,
        )
        flow.request.headers[b'Authorization'] = negotiate


async def generate_spnego_negotiate(cache: KerberosCache, username: str, authority: str) -> str:
    host = authority.split(':')[0]
    principal = await cache.login(username)

    def _generate_spnego_negotiate_blocking(host: str, principal: str) -> str:
        LOGGER.info('generating Negotiate token for host=%s and principal=%s', host, principal)
        name = gssapi.Name(principal, gssapi.NameType.kerberos_principal)
        creds = gssapi.Credentials(name=name, usage="initiate")

        gssapi_auth = HTTPSPNEGOAuth(
            creds=creds,
            opportunistic_auth=True,
            target_name="HTTP",
        )
        return gssapi_auth.generate_request_header(None, host, True)

    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(
        None, _generate_spnego_negotiate_blocking, host, principal
    )
