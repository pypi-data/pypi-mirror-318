import time
import hashlib
import pickle
from typing import Dict, Any, Optional
from .response import Response

class CacheEntry:
    def __init__(self, response: Response, ttl: int):
        self.response = response
        self.expires_at = time.time() + ttl

    @property
    def is_expired(self) -> bool:
        return time.time() > self.expires_at

class CacheManager:
    def __init__(self, ttl: int = 300):
        self._cache: Dict[str, CacheEntry] = {}
        self.default_ttl = ttl

    def _generate_key(self, method: str, url: str, kwargs: Dict[str, Any]) -> str:
        cache_data = f"{method}:{url}:{sorted(kwargs.items())}"
        return hashlib.sha256(cache_data.encode()).hexdigest()

    async def get(self, method: str, url: str, kwargs: Dict[str, Any]) -> Optional[Response]:
        key = self._generate_key(method, url, kwargs)
        entry = self._cache.get(key)
        
        if entry and not entry.is_expired:
            return pickle.loads(pickle.dumps(entry.response))
        
        if entry:
            del self._cache[key]
        return None

    async def set(self, method: str, url: str, kwargs: Dict[str, Any], response: Response, ttl: Optional[int] = None):
        if not response.ok:
            return
        
        key = self._generate_key(method, url, kwargs)
        self._cache[key] = CacheEntry(response, ttl or self.default_ttl)

    def clear(self):
        self._cache.clear()

    def remove(self, method: str, url: str, kwargs: Dict[str, Any]):
        key = self._generate_key(method, url, kwargs)
        self._cache.pop(key, None)
