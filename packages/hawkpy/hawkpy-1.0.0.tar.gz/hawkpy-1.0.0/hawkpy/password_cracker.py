import hashlib
import itertools
import string
from concurrent.futures import ThreadPoolExecutor

class PasswordCracker:
    def __init__(self):
        self.common_passwords = [
            "123456", "password", "12345678", "qwerty",
            "abc123", "111111", "123123", "admin"
        ]
        self.chars = string.ascii_letters + string.digits + string.punctuation

    def crack(self, hash_value, method='dictionary'):
        """Versucht einen Hash zu cracken"""
        if method == 'dictionary':
            return self.dictionary_attack(hash_value)
        elif method == 'brute_force':
            return self.brute_force_attack(hash_value)
        else:
            raise ValueError("Ungültige Methode")

    def dictionary_attack(self, hash_value):
        """Führt einen Dictionary-Angriff durch"""
        for password in self.common_passwords:
            if self._check_hash(password, hash_value):
                return password
        return None

    def brute_force_attack(self, hash_value, max_length=8):
        """Führt einen Brute-Force-Angriff durch"""
        with ThreadPoolExecutor(max_workers=4) as executor:
            for length in range(1, max_length + 1):
                combinations = itertools.product(self.chars, repeat=length)
                futures = []
                
                for combo in combinations:
                    password = ''.join(combo)
                    future = executor.submit(self._check_hash, password, hash_value)
                    futures.append((password, future))
                
                for password, future in futures:
                    if future.result():
                        return password
        
        return None

    def _check_hash(self, password, hash_value):
        """Überprüft, ob ein Passwort zum Hash passt"""
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        return password_hash == hash_value 