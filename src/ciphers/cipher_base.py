"""
CipherSafe Cipher Base Module (cipher_base.py)
---------------------------------------------
Abstract base class for all CipherSafe encryption modules.
Provides a unified interface and structure for encryption systems
like Vigenère and Vernam (One-Time Pad).
"""

from abc import ABC, abstractmethod

class CipherBase(ABC):
    """
    Abstract base class for all CipherSafe ciphers.

    Defines the contract for any encryption system — ensuring that
    each derived cipher implements core cryptographic methods 
    consistently.
    """

    @abstractmethod
    def encrypt(self, plaintext, key):
        """
        Encrypts a plaintext message using a provided key.

        Args:
            plaintext (str): The plaintext message to encrypt.
            key (str): The encryption key.

        Returns:
            str: Encrypted ciphertext.
        """
        pass

    @abstractmethod
    def decrypt(self, ciphertext, key):
        """
        Decrypts a ciphertext message using a provided key.

        Args:
            ciphertext (str): The encrypted message.
            key (str): The key used for encryption.

        Returns:
            str: Decrypted plaintext.
        """
        pass

    @staticmethod
    def _prepare_text(text):
        """
        Preprocesses input by removing non-alphabetic characters
        and converting to uppercase.

        Args:
            text (str): Raw input text.

        Returns:
            str: Sanitized uppercase text.
        """
        return ''.join(char.upper() for char in text if char.isalpha())

    @staticmethod
    def _is_valid_key(key):
        """
        Validates that the provided key is alphabetic and not empty.

        Args:
            key (str): Key to validate.

        Returns:
            bool: True if valid, otherwise False.
        """
        return bool(key) and key.isalpha()


# Optional demonstration for developers
if __name__ == "__main__":
    class DummyCipher(CipherBase):
        """Minimal demonstration subclass."""

        def encrypt(self, plaintext, key):
            return plaintext[::-1]  # Reverse text (toy example)

        def decrypt(self, ciphertext, key):
            return ciphertext[::-1]

    print("=== CipherSafe Base Class Demo ===")
    dummy = DummyCipher()
    text = "HELLOAGENT"
    key = "TEST"
    encrypted = dummy.encrypt(text, key)
    decrypted = dummy.decrypt(encrypted, key)

    print(f"Text:       {text}")
    print(f"Encrypted:  {encrypted}")
    print(f"Decrypted:  {decrypted}")
