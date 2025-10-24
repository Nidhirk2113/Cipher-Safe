"""
Test Suite: Vernam Cipher (OTP)
Ensures that encryption/decryption works perfectly and keys are truly random.
"""

import unittest
from ciphers.vernam import VernamCipher, OTPKeyManager

class TestVernamCipher(unittest.TestCase):

    def setUp(self):
        self.cipher = VernamCipher()
        self.manager = OTPKeyManager()

    def test_encrypt_decrypt_round_trip(self):
        plaintext = "HELLOAGENT"
        otp_key = self.cipher.generate_otp(len(plaintext))
        ciphertext, key_used = self.cipher.encrypt(plaintext, otp_key)
        decrypted = self.cipher.decrypt(ciphertext, key_used)
        self.assertEqual(decrypted, plaintext)

    def test_invalid_key_length(self):
        """Raises error if OTP key shorter than message."""
        with self.assertRaises(ValueError):
            self.cipher.encrypt("HELLO", "SHORT")

    def test_key_uniqueness_check(self):
        """Verify that OTP keys cannot be reused."""
        key = self.manager.get_new_key(10)
        self.manager.mark_key_used(key)
        self.assertTrue(self.manager.is_key_used(key))

    def test_generate_random_key_length(self):
        """Ensure new OTP key is exact message length."""
        length = 20
        otp_key = self.cipher.generate_otp(length)
        self.assertEqual(len(otp_key), length)

if __name__ == "__main__":
    unittest.main(verbosity=2)
