from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from base64 import b64encode, b64decode
import os
from typing import Dict, Any

class EncryptionLayer:
    def __init__(self, key: str = None):
        if key is None:
            key = Fernet.generate_key()
        elif isinstance(key, str):
            key = self._derive_key(key)
        
        self.fernet = Fernet(key)
        self._key = key

    def _derive_key(self, password: str) -> bytes:
        salt = b'modularis_salt'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=480000,
        )
        key = b64encode(kdf.derive(password.encode()))
        return key

    async def encrypt_request(self, kwargs: Dict[str, Any]) -> Dict[str, Any]:
        if 'data' in kwargs:
            kwargs['data'] = self.fernet.encrypt(kwargs['data'])
        if 'json' in kwargs:
            json_str = str(kwargs['json']).encode()
            kwargs['data'] = self.fernet.encrypt(json_str)
            del kwargs['json']
        return kwargs

    async def decrypt_response(self, data: bytes) -> bytes:
        try:
            return self.fernet.decrypt(data)
        except:
            return data

    def rotate_key(self):
        new_key = Fernet.generate_key()
        new_fernet = Fernet(new_key)
        self.fernet = new_fernet
        self._key = new_key
        return new_key

    @property
    def key(self) -> bytes:
        return self._key
