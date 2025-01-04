from cryptography.fernet import Fernet
from base64 import b64encode, b64decode
import hashlib
import os

class Crypto:
    def __init__(self):
        self.key = None
        self.fernet = None

    def generate_key(self):
        """Generiert einen neuen Verschlüsselungsschlüssel"""
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)
        return self.key

    def load_key(self, key):
        """Lädt einen existierenden Schlüssel"""
        self.key = key
        self.fernet = Fernet(self.key)

    def encrypt_data(self, data):
        """Verschlüsselt Daten"""
        if not self.fernet:
            self.generate_key()
        
        if isinstance(data, str):
            data = data.encode()
        
        return self.fernet.encrypt(data)

    def decrypt_data(self, encrypted_data):
        """Entschlüsselt Daten"""
        if not self.fernet:
            raise ValueError("Kein Schlüssel geladen")
        
        return self.fernet.decrypt(encrypted_data)

    @staticmethod
    def hash_password(password, salt=None):
        """Hasht ein Passwort mit Salt"""
        if salt is None:
            salt = os.urandom(32)
        
        key = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt,
            100000
        )
        
        return salt + key 