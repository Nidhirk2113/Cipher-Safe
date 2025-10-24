"""
CipherSafe Key Generator (key_generator.py)
-------------------------------------------
Handles creation of random keys for encryption systems.
Uses cryptographically secure randomness suitable for
Vigenère (keywords) and Vernam (One-Time Pad) ciphers.
"""

import secrets
import string

class KeyGenerator:
    """Generates secure, random cryptographic keys."""

    def __init__(self):
        self.alphabet = string.ascii_uppercase

    def generate_vigenere_key(self, length=6):
        """
        Generate random uppercase keyword for Vigenère cipher.

        Args:
            length (int): Desired key length (default 6).

        Returns:
            str: Secure random uppercase keyword.
        """
        return ''.join(secrets.choice(self.alphabet) for _ in range(length))

    def generate_otp_key(self, length):
        """
        Generate random key for Vernam (OTP) cipher.

        Args:
            length (int): Must match plaintext length.

        Returns:
            str: Truly random key of specified length.
        """
        return ''.join(secrets.choice(self.alphabet) for _ in range(length))


if __name__ == "__main__":
    gen = KeyGenerator()
    print("=== CipherSafe Key Generator Demo ===")
    print(f"Vigenère Key (6): {gen.generate_vigenere_key()}")
    print(f"OTP Key (20): {gen.generate_otp_key(20)}")
