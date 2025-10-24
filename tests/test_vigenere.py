"""
Test Suite: Vigenère Cipher
Ensures correct encryption/decryption behavior using known test vectors.
"""

import unittest
from ciphers.vigenere import VigenereCipher

class TestVigenereCipher(unittest.TestCase):

    def setUp(self):
        """Initialize cipher before each test case."""
        self.cipher = VigenereCipher()
        self.keyword = "LEMON"

    def test_encrypt_basic(self):
        plaintext = "ATTACKATDAWN"
        expected_ciphertext = "LXFOPVEFRNHR"
        result = self.cipher.encrypt(plaintext, self.keyword)
        self.assertEqual(result, expected_ciphertext)

    def test_decrypt_basic(self):
        ciphertext = "LXFOPVEFRNHR"
        expected_plaintext = "ATTACKATDAWN"
        result = self.cipher.decrypt(ciphertext, self.keyword)
        self.assertEqual(result, expected_plaintext)

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            self.cipher.encrypt("", self.keyword)

    def test_empty_key(self):
        with self.assertRaises(ValueError):
            self.cipher.encrypt("HELLO", "")

    def test_round_trip_consistency(self):
        """Ensure that decrypt(encrypt(M)) always returns the original message."""
        text = "MEETMEATNOON"
        key = "GHOST"
        encrypted = self.cipher.encrypt(text, key)
        decrypted = self.cipher.decrypt(encrypted, key)
        self.assertEqual(decrypted, text)

if __name__ == "__main__":
    unittest.main(verbosity=2)
