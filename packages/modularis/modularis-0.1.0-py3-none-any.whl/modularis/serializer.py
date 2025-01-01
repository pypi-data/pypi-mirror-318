import json
import msgpack
from typing import Any, Union, Dict

class Serializer:
    def __init__(self, format: str = 'json'):
        self.format = format.lower()
        self._serializers = {
            'json': self._json_serializer,
            'msgpack': self._msgpack_serializer
        }

    def _json_serializer(self, data: Any) -> bytes:
        return json.dumps(data).encode()

    def _json_deserializer(self, data: bytes) -> Any:
        return json.loads(data.decode())

    def _msgpack_serializer(self, data: Any) -> bytes:
        return msgpack.packb(data)

    def _msgpack_deserializer(self, data: bytes) -> Any:
        return msgpack.unpackb(data)

    def serialize(self, data: Any) -> bytes:
        if self.format not in self._serializers:
            raise ValueError(f"Unsupported format: {self.format}")
        return self._serializers[self.format](data)

    def deserialize(self, data: bytes) -> Any:
        if self.format == 'json':
            return self._json_deserializer(data)
        elif self.format == 'msgpack':
            return self._msgpack_deserializer(data)
        else:
            raise ValueError(f"Unsupported format: {self.format}")

    def set_format(self, format: str):
        if format not in self._serializers:
            raise ValueError(f"Unsupported format: {format}")
        self.format = format.lower()
