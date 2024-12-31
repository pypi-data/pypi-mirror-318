from collections import OrderedDict
import time
from typing import Any, Optional


class PromptCache:
    """
    A simple cache for prompts.
    """

    def __init__(self, default_ttl: int = 3600):
        """
        Initialize the cache.
        default_ttl: The default TTL for prompts in seconds. 0 means no caching.
        """
        self._cache: OrderedDict = OrderedDict()
        self._expiration: dict = {}
        self._default_ttl: int = default_ttl

    def get(self, key: str, version: Optional[str] = None) -> Optional[Any]:
        """
        Get a prompt from the cache.
        """
        cache_key = self._calculate_key(key, version)
        if self._default_ttl == 0:
            return None  # Cache is disabled
        if cache_key in self._cache:
            if self._is_expired(cache_key):
                self.delete(cache_key)
                return None
            self._cache.move_to_end(cache_key)
            return self._cache[cache_key]
        return None

    def set(self, key: str, version: Optional[str] = None, value: Any = None, ttl: Optional[int] = None):
        """
        Set a prompt in the cache.
        """
        ttl = ttl if ttl is not None else self._default_ttl
        cache_key = self._calculate_key(key, version)
        if ttl == 0:
            return  # Don't cache if TTL is 0
        if cache_key in self._cache:
            del self._cache[cache_key]
        self._cache[cache_key] = value
        self._expiration[cache_key] = time.time() + (ttl or self._default_ttl)
        self._cache.move_to_end(cache_key)

    def delete(self, key: str, version: Optional[str] = None):
        """
        Delete a prompt from the cache.
        """
        cache_key = self._calculate_key(key, version)
        if cache_key in self._cache:
            del self._cache[cache_key]
            del self._expiration[cache_key]

    def clear(self):
        """
        Clear the cache.
        """
        self._cache.clear()
        self._expiration.clear()

    def _is_expired(self, key: str) -> bool:
        """
        Check if a prompt is expired.
        """
        return time.time() > self._expiration[key]

    def set_default_ttl(self, ttl: int):
        """
        Set the default TTL for prompts.
        """
        self._default_ttl = ttl

    def _calculate_key(self, key: str, version: Optional[str] = None) -> str:
        return f"{key}:{version}" if version else key

    def __len__(self):
        """
        Gets the number of prompts in the cache.
        """
        return len(self._cache)

    def __contains__(self, key: str) -> bool:
        """
        Check if a prompt is in the cache.
        """
        return key in self._cache and not self._is_expired(key)
