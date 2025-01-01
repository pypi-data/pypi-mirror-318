import zlib
from typing import Dict, Any, Union

class CompressionEngine:
    def __init__(self, level: int = 6):
        self.level = level

    async def compress_request(self, kwargs: Dict[str, Any]) -> Dict[str, Any]:
        headers = kwargs.get('headers', {})
        
        if 'data' in kwargs and isinstance(kwargs['data'], (str, bytes)):
            data = kwargs['data']
            if isinstance(data, str):
                data = data.encode()
            
            compressed = zlib.compress(data, self.level)
            kwargs['data'] = compressed
            headers['Content-Encoding'] = 'deflate'
        
        if 'json' in kwargs:
            json_str = str(kwargs['json']).encode()
            compressed = zlib.compress(json_str, self.level)
            kwargs['data'] = compressed
            headers['Content-Encoding'] = 'deflate'
            del kwargs['json']
        
        kwargs['headers'] = headers
        return kwargs

    async def decompress_response(self, data: Union[bytes, str]) -> Union[bytes, str]:
        if isinstance(data, str):
            data = data.encode()
        
        try:
            return zlib.decompress(data)
        except:
            return data

    def set_compression_level(self, level: int):
        if not 0 <= level <= 9:
            raise ValueError("Compression level must be between 0 and 9")
        self.level = level
