"""
CipherSafe OTP Manager (otp_manager.py)
---------------------------------------
Tracks one-time pad key usage, preventing reuse.
Integrates with key storage to ensure OTP compliance.
"""

from src.key_management.key_generator import KeyGenerator

class OTPKeyManager:
    """Manager for Vernam (One-Time Pad) key operations."""

    def __init__(self):
        self.key_gen = KeyGenerator()
        self.used_keys = set()

    def get_new_key(self, length):
        """
        Generate a unique random OTP key that hasn’t been used before.

        Args:
            length (int): Required key length.

        Returns:
            str: New, unique OTP key.
        """
        while True:
            key = self.key_gen.generate_otp_key(length)
            if key not in self.used_keys:
                return key

    def mark_key_used(self, key):
        """Mark a key as permanently used."""
        self.used_keys.add(key)

    def is_key_used(self, key):
        """
        Check whether a key has already been used.

        Args:
            key (str): Key to check.

        Returns:
            bool: True if key has been used, False otherwise.
        """
        return key in self.used_keys

    def clear_all_keys(self):
        """Reset key usage registry (educational/demo purpose)."""
        self.used_keys.clear()


if __name__ == "__main__":
    manager = OTPKeyManager()
    print("=== OTP Key Manager Demo ===")

    k1 = manager.get_new_key(10)
    print(f"New Key: {k1}")
    manager.mark_key_used(k1)
    print(f"Reused? {manager.is_key_used(k1)}")
