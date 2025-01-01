import asyncio
import aiohttp
from typing import Dict, Any, Optional, List
from dataclasses import dataclass

from urllib.parse import urljoin
from .response import Response
from .middleware import Middleware
from .interceptor import Interceptor
from .cache import CacheManager
from .encryption import EncryptionLayer
from .compression import CompressionEngine
from .serializer import Serializer
from .validator import SchemaValidator
from .metrics import MetricsCollector

@dataclass
class ClientConfig:
    base_url: str = ""
    timeout: int = 30
    max_retries: int = 3
    compression_enabled: bool = True
    encryption_enabled: bool = False
    cache_enabled: bool = True
    metrics_enabled: bool = True
    schema_validation: bool = True

class Client:
    def __init__(self, config: Optional[ClientConfig] = None):
        self.config = config or ClientConfig()
        self.session = None
        self._setup_components()
    
    def _setup_components(self):
        self.cache = CacheManager()
        self.encryption = EncryptionLayer()
        self.compression = CompressionEngine()
        self.serializer = Serializer()
        self.validator = SchemaValidator()
        self.metrics = MetricsCollector()
        self.middleware = []
        self.interceptors = []
    
    async def __aenter__(self):
        timeout = aiohttp.ClientTimeout(total=self.config.timeout)
        self.session = aiohttp.ClientSession(timeout=timeout)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
    
    def add_middleware(self, middleware: Middleware):
        self.middleware.append(middleware)
    
    def add_interceptor(self, interceptor: Interceptor):
        self.interceptors.append(interceptor)
    
    async def _process_request(self, method: str, url: str, **kwargs):
        if not url.startswith(('http://', 'https://')):
            url = urljoin(self.config.base_url, url)

        if self.config.schema_validation and 'schema' in kwargs:
            self.validator.validate_request(kwargs, kwargs.pop('schema'))
        
        if self.config.cache_enabled:
            cached_response = await self.cache.get(method, url, kwargs)
            if cached_response:
                return cached_response
        
        for interceptor in self.interceptors:
            kwargs = await interceptor.before_request(method, url, kwargs)
        
        if self.config.compression_enabled and 'data' in kwargs:
            kwargs['data'] = await self.compression.compress_request(kwargs['data'])
        
        if self.config.encryption_enabled and 'data' in kwargs:
            kwargs['data'] = await self.encryption.encrypt_request(kwargs['data'])
        
        retry_count = 0
        while retry_count < self.config.max_retries:
            try:
                async with self.session.request(method, url, **kwargs) as response:
                    response_data = await response.read()
                    
                    if self.config.encryption_enabled:
                        response_data = await self.encryption.decrypt_response(response_data)
                    
                    if self.config.compression_enabled:
                        response_data = await self.compression.decompress_response(response_data)
                    
                    response_obj = Response(
                        status=response.status,
                        headers=dict(response.headers),
                        data=response_data,
                        url=str(response.url)
                    )
                    
                    for interceptor in reversed(self.interceptors):
                        response_obj = await interceptor.after_response(response_obj)
                    
                    if self.config.cache_enabled and response_obj.ok:
                        await self.cache.set(method, url, kwargs, response_obj)
                    
                    if self.config.metrics_enabled:
                        self.metrics.record_request(method, url, response_obj)
                    
                    return response_obj
                    
            except (aiohttp.ClientError, asyncio.TimeoutError) as e:
                retry_count += 1
                if retry_count >= self.config.max_retries:
                    raise Exception(f"Request failed after {retry_count} retries: {str(e)}")
                await asyncio.sleep(1 * retry_count)  # Exponential backoff
    
    async def get(self, url: str, **kwargs):
        return await self._process_request("GET", url, **kwargs)
    
    async def post(self, url: str, **kwargs):
        return await self._process_request("POST", url, **kwargs)
    
    async def put(self, url: str, **kwargs):
        return await self._process_request("PUT", url, **kwargs)
    
    async def delete(self, url: str, **kwargs):
        return await self._process_request("DELETE", url, **kwargs)
    
    async def patch(self, url: str, **kwargs):
        return await self._process_request("PATCH", url, **kwargs)
