"""
CipherSafe Vernam Cipher Module (vernam.py)
-------------------------------------------
Implements the One-Time Pad (OTP) cipher — the only mathematically 
unbreakable encryption when properly used.
"""

import secrets
import string

class VernamCipher:
    """
    Vernam (One-Time Pad) Cipher Implementation.

    Perfect secrecy is achieved if:
    1. The key is truly random.
    2. The key is at least as long as the message.
    3. The key is used only once.
    4. The key remains completely secret.
    """

    def __init__(self):
        self.alphabet = string.ascii_uppercase

    def _prepare_text(self, text):
        """Sanitizes input: removes non-alphabet chars and converts to uppercase."""
        return ''.join(char.upper() for char in text if char.isalpha())

    def generate_otp(self, length):
        """
        Generates a truly random OTP key of given length using Python's secrets module.

        Args:
            length (int): Length of plaintext message.

        Returns:
            str: Random uppercase key of same length.
        """
        return ''.join(secrets.choice(self.alphabet) for _ in range(length))

    def encrypt(self, plaintext, otp_key=None):
        """
        Encrypt plaintext using Vernam cipher.

        Args:
            plaintext (str): Message to encrypt.
            otp_key (str): Optional existing key; otherwise generated.

        Returns:
            tuple: (ciphertext, otp_key)
        """
        plaintext = self._prepare_text(plaintext)

        # Generate random key if not provided
        if otp_key is None:
            otp_key = self.generate_otp(len(plaintext))
        else:
            otp_key = self._prepare_text(otp_key)

        if len(otp_key) < len(plaintext):
            raise ValueError("OTP key must be at least as long as the plaintext.")

        ciphertext = []
        for i in range(len(plaintext)):
            p = ord(plaintext[i]) - ord('A')
            k = ord(otp_key[i]) - ord('A')
            c = (p + k) % 26
            ciphertext.append(chr(c + ord('A')))

        return ''.join(ciphertext), otp_key

    def decrypt(self, ciphertext, otp_key):
        """
        Decrypt Vernam cipher (One-Time Pad).

        Args:
            ciphertext (str): Encrypted ciphertext.
            otp_key (str): Key used for encryption.

        Returns:
            str: The decrypted plaintext message.
        """
        ciphertext = self._prepare_text(ciphertext)
        otp_key = self._prepare_text(otp_key)

        if len(otp_key) < len(ciphertext):
            raise ValueError("OTP key must be at least as long as the ciphertext.")

        plaintext = []
        for i in range(len(ciphertext)):
            c = ord(ciphertext[i]) - ord('A')
            k = ord(otp_key[i]) - ord('A')
            p = (c - k + 26) % 26
            plaintext.append(chr(p + ord('A')))

        return ''.join(plaintext)


class OTPKeyManager:
    """
    Key manager for OTP lifecycle and single-use enforcement.

    Ensures that each OTP key is unique and never reused.
    """

    def __init__(self):
        self.used_keys = set()
        self.cipher = VernamCipher()

    def get_new_key(self, length):
        """Generate a unique unused OTP key."""
        while True:
            key = self.cipher.generate_otp(length)
            if key not in self.used_keys:
                return key

    def mark_key_used(self, key):
        """Records a key as used."""
        self.used_keys.add(key)

    def is_key_used(self, key):
        """
        Checks if a given OTP key has already been used.

        Returns:
            bool: True if key is used, False if new.
        """
        return key in self.used_keys


# Demonstration (when run standalone)
if __name__ == "__main__":
    print("=== CipherSafe Vernam Cipher Demo ===")
    cipher = VernamCipher()
    manager = OTPKeyManager()

    plaintext = "INFILTRATE FACILITY AT MIDNIGHT"
    otp_key = manager.get_new_key(len(plaintext))

    print(f"Plaintext:  {plaintext}")
    print(f"OTP Key:    {otp_key}")

    ciphertext, used_key = cipher.encrypt(plaintext, otp_key)
    print(f"Ciphertext: {ciphertext}")

    decrypted = cipher.decrypt(ciphertext, used_key)
    manager.mark_key_used(used_key)

    print(f"Decrypted:  {decrypted}")
    print(f"Match: {plaintext.replace(' ', '') == decrypted}")
