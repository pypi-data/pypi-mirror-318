"""
Modularis Middleware Module
=========================

Middleware system for the Modularis HTTP client.

Author: Hexakleo
GitHub: https://github.com/hexakleo
Twitter: @hexakleo
LinkedIn: https://linkedin.com/in/hexakleo

Copyright (c) 2024 Hexakleo. All rights reserved.
Licensed under the MIT License.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, Callable, Awaitable


class Middleware(ABC):
    """
    Abstract base class for HTTP client middleware.

    Middleware provides a way to modify requests and responses
    by implementing hooks that are called before and after
    each request.

    Example:
        >>> class LoggingMiddleware(Middleware):
        ...     async def process(self, request: Any, next: Callable) -> Any:
        ...         print(f"Making request to: {request['url']}")
        ...         response = await next(request)
        ...         print(f"Got response with status: {response['status']}")
        ...         return response
        ...
        >>> client.add_middleware(LoggingMiddleware())
    """

    @abstractmethod
    async def process(
        self,
        request: Any,
        next: Callable[..., Awaitable[Any]]
    ) -> Any:
        """
        Process a request and its response.

        This method is called for each request, allowing the middleware
        to modify both the request and response.

        Args:
            request (Any): Request data including method, url, headers, and body
            next (Callable[..., Awaitable[Any]]): Next middleware in the chain

        Returns:
            Any: The response from the next middleware
        """
        pass


class MiddlewareChain:
    """
    A chain of middleware that executes in sequence.

    This class manages a list of middleware and executes them in order,
    passing the request through each one before reaching the handler.

    Example:
        >>> chain = MiddlewareChain([
        ...     LoggingMiddleware(),
        ...     AuthMiddleware(),
        ...     CacheMiddleware()
        ... ])
        >>> response = await chain.execute(request, handler)
    """

    def __init__(self, middleware_list: list[Middleware]) -> None:
        """
        Initialize the middleware chain.

        Args:
            middleware_list (list[Middleware]): List of middleware instances
        """
        self.middleware = middleware_list

    async def execute(
        self,
        request: Any,
        handler: Callable[..., Awaitable[Any]]
    ) -> Any:
        """
        Execute all middleware in sequence.

        Args:
            request (Any): Request data
            handler (Callable[..., Awaitable[Any]]): Final request handler

        Returns:
            Any: Response after processing through all middleware
        """
        async def create_chain(index: int) -> Any:
            if index >= len(self.middleware):
                return await handler(request)
            
            async def next_middleware(req: Any) -> Any:
                return await create_chain(index + 1)
            
            return await self.middleware[index].process(request, next_middleware)
        
        return await create_chain(0)


class LoggingMiddleware(Middleware):
    """
    Middleware for logging requests and responses.

    This middleware logs details about each request and response,
    including timing information and status codes.

    Example:
        >>> import logging
        >>> logging.basicConfig(level=logging.INFO)
        >>> client.add_middleware(LoggingMiddleware())
    """

    def __init__(self, logger: Optional[Any] = None) -> None:
        """
        Initialize the logging middleware.

        Args:
            logger (Optional[Any]): Logger instance to use
        """
        import logging
        self.logger = logger or logging.getLogger(__name__)

    async def process(
        self,
        request: Any,
        next: Callable[..., Awaitable[Any]]
    ) -> Any:
        """
        Log request and response details.

        Args:
            request (Any): Request data
            next (Callable[..., Awaitable[Any]]): Next middleware

        Returns:
            Any: Response from next middleware
        """
        self.logger.info(
            f"Making {request.get('method')} request to {request.get('url')}"
        )
        
        response = await next(request)
        
        self.logger.info(
            f"Got response: {response.get('status')} for {response.get('url')}"
        )
        
        return response


class TimingMiddleware(Middleware):
    """
    Middleware for measuring request timing.

    This middleware tracks the time taken for each request
    and can report statistics about request performance.

    Example:
        >>> client.add_middleware(TimingMiddleware())
    """

    def __init__(self) -> None:
        """Initialize the timing middleware."""
        self.times = []

    async def process(
        self,
        request: Any,
        next: Callable[..., Awaitable[Any]]
    ) -> Any:
        """
        Time the request processing.

        Args:
            request (Any): Request data
            next (Callable[..., Awaitable[Any]]): Next middleware

        Returns:
            Any: Response from next middleware
        """
        import time
        start_time = time.time()
        
        response = await next(request)
        
        duration = time.time() - start_time
        self.times.append(duration)
        
        if isinstance(response, dict):
            response['duration'] = duration
        
        return response

    def get_statistics(self) -> Dict[str, float]:
        """
        Get timing statistics for all requests.

        Returns:
            Dict[str, float]: Statistics including min, max, and average times
        """
        if not self.times:
            return {"min": 0, "max": 0, "avg": 0, "total": 0}

        return {
            "min": min(self.times),
            "max": max(self.times),
            "avg": sum(self.times) / len(self.times),
            "total": sum(self.times)
        }
