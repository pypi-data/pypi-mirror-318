"""
Modularis HTTP Client Module
===========================

A high-performance, modular HTTP client for Python with advanced features.

Author: Hexakleo
GitHub: https://github.com/hexakleo
Twitter: @hexakleo
LinkedIn: https://linkedin.com/in/hexakleo

Copyright (c) 2024 Hexakleo. All rights reserved.
Licensed under the MIT License.
"""

import asyncio
import aiohttp
from typing import Dict, Any, Optional, List, Union
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
    """
    Configuration class for the HTTP client.

    Attributes:
        base_url (str): Base URL for all requests
        timeout (int): Request timeout in seconds
        max_retries (int): Maximum number of retry attempts
        compression_enabled (bool): Enable response compression
        encryption_enabled (bool): Enable request/response encryption
        cache_enabled (bool): Enable response caching
        metrics_enabled (bool): Enable request metrics collection
        schema_validation (bool): Enable request/response schema validation
    """
    base_url: str = ""
    timeout: int = 30
    max_retries: int = 3
    compression_enabled: bool = True
    encryption_enabled: bool = False
    cache_enabled: bool = True
    metrics_enabled: bool = True
    schema_validation: bool = True


class Client:
    """
    A powerful, feature-rich HTTP client with support for middleware,
    interceptors, caching, encryption, compression, and metrics collection.

    Features:
        - Asynchronous request handling
        - Automatic retries with exponential backoff
        - Request/Response transformation
        - Middleware and interceptor support
        - Built-in caching
        - Data compression
        - End-to-end encryption
        - Schema validation
        - Metrics collection

    Example:
        >>> from modularis import Client, ClientConfig
        >>> 
        >>> config = ClientConfig(
        ...     base_url="https://api.example.com",
        ...     timeout=30,
        ...     max_retries=3
        ... )
        >>> 
        >>> async with Client(config) as client:
        ...     response = await client.get("/users/1")
        ...     print(response.data)
    """

    def __init__(self, config: Optional[ClientConfig] = None) -> None:
        """
        Initialize a new HTTP client instance.

        Args:
            config (Optional[ClientConfig]): Client configuration
        """
        self.config = config or ClientConfig()
        self.session = None
        self._setup_components()

    def _setup_components(self) -> None:
        """Initialize all client components and features."""
        self.cache = CacheManager()
        self.encryption = EncryptionLayer()
        self.compression = CompressionEngine()
        self.serializer = Serializer()
        self.validator = SchemaValidator()
        self.metrics = MetricsCollector()
        self.middleware: List[Middleware] = []
        self.interceptors: List[Interceptor] = []

    async def __aenter__(self) -> 'Client':
        """Set up the async context manager."""
        timeout = aiohttp.ClientTimeout(total=self.config.timeout)
        self.session = aiohttp.ClientSession(timeout=timeout)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """Clean up the async context manager."""
        if self.session:
            await self.session.close()

    def add_middleware(self, middleware: Middleware) -> None:
        """
        Add a middleware to the client.

        Args:
            middleware (Middleware): Middleware instance to add
        """
        self.middleware.append(middleware)

    def add_interceptor(self, interceptor: Interceptor) -> None:
        """
        Add an interceptor to the client.

        Args:
            interceptor (Interceptor): Interceptor instance to add
        """
        self.interceptors.append(interceptor)

    async def _process_request(
        self,
        method: str,
        url: str,
        **kwargs: Any
    ) -> Response:
        """
        Process and execute an HTTP request.

        Args:
            method (str): HTTP method (GET, POST, etc.)
            url (str): Request URL
            **kwargs: Additional request parameters

        Returns:
            Response: Response object containing status, headers, and data

        Raises:
            Exception: If request fails after all retries
        """
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
                        response_data = await self.encryption.decrypt_response(
                            response_data
                        )

                    if self.config.compression_enabled:
                        response_data = await self.compression.decompress_response(
                            response_data
                        )

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
                    raise Exception(
                        f"Request failed after {retry_count} retries: {str(e)}"
                    )
                await asyncio.sleep(1 * retry_count)  # Exponential backoff

    async def get(self, url: str, **kwargs: Any) -> Response:
        """
        Send a GET request.

        Args:
            url (str): Request URL
            **kwargs: Additional request parameters

        Returns:
            Response: Response object
        """
        return await self._process_request("GET", url, **kwargs)

    async def post(self, url: str, **kwargs: Any) -> Response:
        """
        Send a POST request.

        Args:
            url (str): Request URL
            **kwargs: Additional request parameters

        Returns:
            Response: Response object
        """
        return await self._process_request("POST", url, **kwargs)

    async def put(self, url: str, **kwargs: Any) -> Response:
        """
        Send a PUT request.

        Args:
            url (str): Request URL
            **kwargs: Additional request parameters

        Returns:
            Response: Response object
        """
        return await self._process_request("PUT", url, **kwargs)

    async def delete(self, url: str, **kwargs: Any) -> Response:
        """
        Send a DELETE request.

        Args:
            url (str): Request URL
            **kwargs: Additional request parameters

        Returns:
            Response: Response object
        """
        return await self._process_request("DELETE", url, **kwargs)

    async def patch(self, url: str, **kwargs: Any) -> Response:
        """
        Send a PATCH request.

        Args:
            url (str): Request URL
            **kwargs: Additional request parameters

        Returns:
            Response: Response object
        """
        return await self._process_request("PATCH", url, **kwargs)
