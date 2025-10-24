"""
CipherSafe Vigenère Cipher Module (vigenere.py)
----------------------------------------------
Implements classical polyalphabetic substitution cipher
for routine communications between agents.
"""

class VigenereCipher:
    """
    Implements Vigenère cipher encryption and decryption.

    The Vigenère cipher uses a repeating keyword to shift each
    character in the plaintext by a varying amount across alphabets.
    """

    def __init__(self):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def _prepare_text(self, text):
        """Cleans and uppercases text, filtering non-alphabet chars."""
        return ''.join(char.upper() for char in text if char.isalpha())

    def _generate_key(self, text, keyword):
        """
        Extend or repeat the keyword to match the text length.

        Args:
            text (str): The input text (plaintext or ciphertext)
            keyword (str): The shared key used for encryption/decryption

        Returns:
            str: Key repeated or truncated to match `text` length.
        """
        keyword = keyword.upper()
        key = []
        key_index = 0

        for char in text:
            if char.isalpha():
                key.append(keyword[key_index % len(keyword)])
                key_index += 1
        return ''.join(key)

    def encrypt(self, plaintext, keyword):
        """
        Encrypts plaintext using the Vigenère cipher formula:

            C_i = (P_i + K_i) mod 26

        Args:
            plaintext (str): The message to encrypt
            keyword (str): The shared key for encryption

        Returns:
            str: The resulting ciphertext
        """
        plaintext = self._prepare_text(plaintext)
        keyword = self._prepare_text(keyword)
        if not keyword:
            raise ValueError("Encryption keyword cannot be empty.")

        key = self._generate_key(plaintext, keyword)
        ciphertext = []

        for i in range(len(plaintext)):
            p = ord(plaintext[i]) - ord('A')
            k = ord(key[i]) - ord('A')
            c = (p + k) % 26
            ciphertext.append(chr(c + ord('A')))

        return ''.join(ciphertext)

    def decrypt(self, ciphertext, keyword):
        """
        Decrypts ciphertext using the Vigenère cipher formula:

            P_i = (C_i - K_i + 26) mod 26

        Args:
            ciphertext (str): The encrypted message
            keyword (str): The shared key used for encryption

        Returns:
            str: The decrypted plaintext
        """
        ciphertext = self._prepare_text(ciphertext)
        keyword = self._prepare_text(keyword)
        if not keyword:
            raise ValueError("Decryption keyword cannot be empty.")

        key = self._generate_key(ciphertext, keyword)
        plaintext = []

        for i in range(len(ciphertext)):
            c = ord(ciphertext[i]) - ord('A')
            k = ord(key[i]) - ord('A')
            p = (c - k + 26) % 26
            plaintext.append(chr(p + ord('A')))

        return ''.join(plaintext)


# Demonstration when run as a standalone script
if __name__ == "__main__":
    cipher = VigenereCipher()
    print("=== CipherSafe Vigenère Cipher Demo ===")
    plaintext = "MEET AT MIDNIGHT HQ"
    keyword = "STEALTH"

    encrypted = cipher.encrypt(plaintext, keyword)
    print(f"Plaintext: {plaintext}")
    print(f"Keyword:   {keyword}")
    print(f"Encrypted: {encrypted}")

    decrypted = cipher.decrypt(encrypted, keyword)
    print(f"Decrypted: {decrypted}")
