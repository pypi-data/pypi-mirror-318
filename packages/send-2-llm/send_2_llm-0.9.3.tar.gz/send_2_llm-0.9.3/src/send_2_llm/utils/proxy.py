"""Proxy configuration for LLM providers."""

from dataclasses import dataclass
from typing import Optional, Dict
import httpx
from enum import Enum


class ProxyType(str, Enum):
    """Types of proxy protocols."""
    HTTP = "http"
    HTTPS = "https"
    SOCKS4 = "socks4"
    SOCKS5 = "socks5"


@dataclass
class ProxyConfig:
    """Proxy configuration."""
    host: str
    port: int
    username: Optional[str] = None
    password: Optional[str] = None
    proxy_type: ProxyType = ProxyType.HTTP

    @property
    def url(self) -> str:
        """Get proxy URL with auth if provided."""
        auth = f"{self.username}:{self.password}@" if self.username and self.password else ""
        return f"{self.proxy_type.value}://{auth}{self.host}:{self.port}"

    def get_httpx_config(self) -> Dict:
        """Get proxy configuration for httpx client."""
        proxy_url = self.url
        return {
            "transport": httpx.AsyncHTTPTransport(
                proxy=httpx.Proxy(
                    url=proxy_url,
                ),
                verify=False
            )
        }


class ProxyManager:
    """Manager for proxy configurations."""
    
    def __init__(self):
        self._proxies: Dict[str, ProxyConfig] = {}
        self._default_proxy: Optional[str] = None

    def add_proxy(self, name: str, config: ProxyConfig, make_default: bool = False):
        """Add proxy configuration."""
        self._proxies[name] = config
        if make_default or not self._default_proxy:
            self._default_proxy = name

    def get_proxy(self, name: Optional[str] = None) -> Optional[ProxyConfig]:
        """Get proxy configuration by name or default."""
        if not name and self._default_proxy:
            name = self._default_proxy
        return self._proxies.get(name)

    def remove_proxy(self, name: str):
        """Remove proxy configuration."""
        if name in self._proxies:
            del self._proxies[name]
            if self._default_proxy == name:
                self._default_proxy = next(iter(self._proxies)) if self._proxies else None

    def create_client(
        self,
        base_url: str,
        headers: Dict,
        name: Optional[str] = None,
        **kwargs
    ) -> httpx.AsyncClient:
        """Create httpx client with proxy configuration.
        
        Args:
            base_url: Base URL for client
            headers: Headers for client
            name: Proxy configuration name
            **kwargs: Additional client parameters
            
        Returns:
            Configured httpx.AsyncClient
        """
        config = {
            "base_url": base_url,
            "headers": headers,
            "timeout": kwargs.get("timeout", 30.0)
        }
        
        proxy = self.get_proxy(name)
        if proxy:
            config.update(proxy.get_httpx_config())
        
        return httpx.AsyncClient(**config)


# Global proxy manager
proxy_manager = ProxyManager() 