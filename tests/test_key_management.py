"""
Test Suite: Key Management
Covers key generation, OTP control, and key persistence.
"""

import unittest
import os
from key_management.key_generator import KeyGenerator
from key_management.otp_manager import OTPKeyManager
from key_management.key_storage import KeyStorage

class TestKeyManagement(unittest.TestCase):

    def setUp(self):
        self.key_gen = KeyGenerator()
        self.otp_mgr = OTPKeyManager()
        self.storage = KeyStorage(storage_path="data/keys_test/")
        os.makedirs("data/keys_test/", exist_ok=True)

    def test_vigenere_key_generation(self):
        key = self.key_gen.generate_vigenere_key(8)
        self.assertTrue(key.isalpha())
        self.assertEqual(len(key), 8)

    def test_otp_key_generation_and_length(self):
        key = self.key_gen.generate_otp_key(12)
        self.assertEqual(len(key), 12)

    def test_otp_manager_key_reuse_prevention(self):
        key = self.otp_mgr.get_new_key(8)
        self.otp_mgr.mark_key_used(key)
        self.assertTrue(self.otp_mgr.is_key_used(key))

    def test_key_storage_save_and_load(self):
        self.storage.save_key("vigenere", "E1", "SECRET")
        keys = self.storage.load_keys("vigenere")
        self.assertIn("E1", keys)

    def tearDown(self):
        # Clean up test directory
        import shutil
        shutil.rmtree("data/keys_test/", ignore_errors=True)

if __name__ == "__main__":
    unittest.main(verbosity=2)
