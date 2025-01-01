"""
Modularis Interceptor Module
==========================

Request/Response interceptors for the Modularis HTTP client.

Author: Hexakleo
GitHub: https://github.com/hexakleo
Twitter: @hexakleo
LinkedIn: https://linkedin.com/in/hexakleo

Copyright (c) 2024 Hexakleo. All rights reserved.
Licensed under the MIT License.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, Union
from .response import Response


class Interceptor(ABC):
    """
    Abstract base class for HTTP client interceptors.

    Interceptors provide a way to modify requests before they are sent
    and responses after they are received. Unlike middleware, interceptors
    operate on the raw request/response data.

    Example:
        >>> class AuthInterceptor(Interceptor):
        ...     def __init__(self, token: str):
        ...         self.token = token
        ...
        ...     def before_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        ...         request.setdefault('headers', {})
        ...         request['headers']['Authorization'] = f'Bearer {self.token}'
        ...         return request
        ...
        >>> client.add_interceptor(AuthInterceptor('my-token'))
    """

    @abstractmethod
    def before_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process a request before it is sent.

        This method is called before each request is made, allowing
        the interceptor to modify or enhance the request data.

        Args:
            request (Dict[str, Any]): Request data including method,
                url, headers, and body

        Returns:
            Dict[str, Any]: Modified request data
        """
        return request

    @abstractmethod
    def after_response(self, response: Response) -> Response:
        """
        Process a response after it is received.

        This method is called after each response is received,
        allowing the interceptor to modify or enhance the response.

        Args:
            response (Response): Response object

        Returns:
            Response: Modified response object
        """
        return response


class AuthInterceptor(Interceptor):
    """
    Interceptor for adding authentication to requests.

    This interceptor adds authentication headers to requests
    using various authentication schemes.

    Example:
        >>> # Bearer token authentication
        >>> auth = AuthInterceptor(token='my-token')
        >>> client.add_interceptor(auth)
        >>>
        >>> # Basic authentication
        >>> auth = AuthInterceptor(username='user', password='pass')
        >>> client.add_interceptor(auth)
    """

    def __init__(
        self,
        token: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        scheme: str = 'Bearer'
    ) -> None:
        """
        Initialize the authentication interceptor.

        Args:
            token (Optional[str]): Authentication token
            username (Optional[str]): Username for basic auth
            password (Optional[str]): Password for basic auth
            scheme (str): Authentication scheme (Bearer, Basic, etc.)
        """
        self.token = token
        self.username = username
        self.password = password
        self.scheme = scheme

    async def before_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Add authentication headers to the request."""
        if 'headers' not in request:
            request['headers'] = {}

        if self.token:
            request['headers']['Authorization'] = f'{self.scheme} {self.token}'
        elif self.username and self.password:
            import base64
            credentials = base64.b64encode(
                f'{self.username}:{self.password}'.encode()
            ).decode()
            request['headers']['Authorization'] = f'Basic {credentials}'

        return request

    async def after_response(self, response: Response) -> Response:
        """Pass through response without modification."""
        return response


class RetryInterceptor(Interceptor):
    """
    Interceptor for implementing retry logic.

    This interceptor automatically retries failed requests
    with exponential backoff.

    Example:
        >>> retry = RetryInterceptor(max_retries=3, retry_codes=[500, 502, 503])
        >>> client.add_interceptor(retry)
    """

    def __init__(
        self,
        max_retries: int = 3,
        retry_codes: list[int] = None,
        backoff_factor: float = 0.1
    ) -> None:
        """
        Initialize the retry interceptor.

        Args:
            max_retries (int): Maximum number of retry attempts
            retry_codes (list[int]): Status codes to retry on
            backoff_factor (float): Exponential backoff factor
        """
        self.max_retries = max_retries
        self.retry_codes = retry_codes or [500, 502, 503, 504]
        self.backoff_factor = backoff_factor
        self._attempt = 0

    async def before_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Track retry attempts."""
        self._attempt += 1
        return request

    async def after_response(self, response: Response) -> Response:
        """
        Handle retry logic based on response.

        If the response status code is in retry_codes and we haven't
        exceeded max_retries, the request will be retried after a
        delay determined by the backoff factor.
        """
        if (
            response.status in self.retry_codes
            and self._attempt < self.max_retries
        ):
            import asyncio
            delay = self.backoff_factor * (2 ** (self._attempt - 1))
            await asyncio.sleep(delay)
            # The actual retry is handled by the client
            return response

        self._attempt = 0
        return response


class CompressionInterceptor(Interceptor):
    """
    Interceptor for compressing request bodies and decompressing responses.

    This interceptor handles various compression algorithms (gzip, deflate)
    automatically based on the Content-Encoding header.

    Example:
        >>> compression = CompressionInterceptor(['gzip', 'deflate'])
        >>> client.add_interceptor(compression)
    """

    def __init__(self, algorithms: list[str] = None) -> None:
        """
        Initialize the compression interceptor.

        Args:
            algorithms (list[str]): Supported compression algorithms
        """
        self.algorithms = algorithms or ['gzip', 'deflate']

    async def before_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """
        Compress request body if needed.

        Adds appropriate headers and compresses the request body
        using the first supported algorithm.
        """
        if 'data' in request and isinstance(request['data'], (str, bytes)):
            import gzip
            import zlib

            if 'gzip' in self.algorithms:
                request['data'] = gzip.compress(
                    request['data'].encode() if isinstance(request['data'], str)
                    else request['data']
                )
                request.setdefault('headers', {})
                request['headers']['Content-Encoding'] = 'gzip'

        return request

    async def after_response(self, response: Response) -> Response:
        """
        Decompress response body if needed.

        Automatically handles decompression based on Content-Encoding header.
        """
        if response.headers.get('content-encoding') in self.algorithms:
            import gzip
            import zlib

            if response.headers['content-encoding'] == 'gzip':
                response.data = gzip.decompress(response.data)
            elif response.headers['content-encoding'] == 'deflate':
                response.data = zlib.decompress(response.data)

        return response
