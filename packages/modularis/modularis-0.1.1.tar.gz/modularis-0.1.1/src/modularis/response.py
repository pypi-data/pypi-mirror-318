"""
Modularis Response Module
========================

Response handling and processing for the Modularis HTTP client.

Author: Hexakleo
GitHub: https://github.com/hexakleo
Twitter: @hexakleo
LinkedIn: https://linkedin.com/in/hexakleo

Copyright (c) 2024 Hexakleo. All rights reserved.
Licensed under the MIT License.
"""

from typing import Dict, Any, Optional, Union
from dataclasses import dataclass
import json
import time


@dataclass
class Response:
    """
    A class representing an HTTP response with enhanced features.

    This class provides a rich interface for handling HTTP responses,
    including automatic JSON parsing, timing information, and convenient
    property access.

    Attributes:
        status (int): HTTP status code
        headers (Dict[str, str]): Response headers
        data (Union[dict, str, bytes]): Response data
        url (str): Request URL
        elapsed (float): Request duration in seconds
        timestamp (float): Response timestamp
        _raw_data (bytes): Raw response data

    Properties:
        ok (bool): True if status code is less than 400
        is_json (bool): True if response is JSON
        is_text (bool): True if response is text
        is_binary (bool): True if response is binary
        content_type (str): Response content type
        encoding (str): Response encoding

    Example:
        >>> response = Response(
        ...     status=200,
        ...     headers={"content-type": "application/json"},
        ...     data=b'{"key": "value"}',
        ...     url="https://api.example.com/endpoint"
        ... )
        >>> 
        >>> print(response.ok)  # True
        >>> print(response.json["key"])  # "value"
    """

    status: int
    headers: Dict[str, str]
    data: Union[dict, str, bytes]
    url: str
    elapsed: float = 0.0
    timestamp: float = time.time()
    _raw_data: Optional[bytes] = None

    def __post_init__(self) -> None:
        """Process the response data after initialization."""
        if isinstance(self.data, bytes):
            self._raw_data = self.data
            self._process_data()

    def _process_data(self) -> None:
        """Process raw response data based on content type."""
        content_type = self.headers.get('content-type', '').lower()

        if 'application/json' in content_type:
            try:
                self.data = json.loads(self._raw_data.decode(self.encoding))
            except (json.JSONDecodeError, UnicodeDecodeError):
                self.data = self._raw_data
        elif 'text/' in content_type:
            try:
                self.data = self._raw_data.decode(self.encoding)
            except UnicodeDecodeError:
                self.data = self._raw_data
        else:
            self.data = self._raw_data

    @property
    def ok(self) -> bool:
        """Check if the response status indicates success."""
        return self.status < 400

    @property
    def is_json(self) -> bool:
        """Check if the response is JSON."""
        return 'application/json' in self.headers.get('content-type', '').lower()

    @property
    def is_text(self) -> bool:
        """Check if the response is text."""
        return 'text/' in self.headers.get('content-type', '').lower()

    @property
    def is_binary(self) -> bool:
        """Check if the response is binary."""
        return not (self.is_json or self.is_text)

    @property
    def content_type(self) -> str:
        """Get the response content type."""
        return self.headers.get('content-type', 'application/octet-stream')

    @property
    def encoding(self) -> str:
        """Get the response encoding."""
        return self.headers.get('content-encoding', 'utf-8')

    @property
    def json(self) -> dict:
        """
        Get the response data as JSON.

        Returns:
            dict: Parsed JSON data

        Raises:
            ValueError: If response is not JSON
            json.JSONDecodeError: If JSON parsing fails
        """
        if not self.is_json:
            raise ValueError("Response is not JSON")
        if isinstance(self.data, (str, bytes)):
            return json.loads(self.data)
        return self.data

    @property
    def text(self) -> str:
        """
        Get the response data as text.

        Returns:
            str: Response text

        Raises:
            ValueError: If response cannot be converted to text
        """
        if isinstance(self.data, bytes):
            return self.data.decode(self.encoding)
        if isinstance(self.data, dict):
            return json.dumps(self.data)
        if isinstance(self.data, str):
            return self.data
        raise ValueError("Cannot convert response to text")

    @property
    def raw(self) -> bytes:
        """
        Get the raw response data.

        Returns:
            bytes: Raw response data
        """
        return self._raw_data if self._raw_data else self.data

    def raise_for_status(self) -> None:
        """
        Raise an exception for failed HTTP status codes.

        Raises:
            HTTPError: If response status indicates an error
        """
        if not self.ok:
            raise HTTPError(f"HTTP {self.status}: {self.text}", response=self)


class HTTPError(Exception):
    """
    Exception raised for failed HTTP responses.

    Attributes:
        message (str): Error message
        response (Response): Response object that caused the error
    """

    def __init__(self, message: str, response: Response) -> None:
        """
        Initialize the HTTP error.

        Args:
            message (str): Error message
            response (Response): Response object
        """
        super().__init__(message)
        self.response = response
