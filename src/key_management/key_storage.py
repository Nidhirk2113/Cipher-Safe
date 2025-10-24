"""
CipherSafe Key Storage Module (key_storage.py)
----------------------------------------------
Handles saving and loading of encryption keys (Vigenère and OTP).
Stored keys are organized in JSON format to maintain persistency
and integrity between sessions.
"""

import json
import os
from datetime import datetime

class KeyStorage:
    """Manages loading and saving of encryption keys."""

    def __init__(self, storage_path="data/keys/"):
        self.storage_path = storage_path
        self.vigenere_file = os.path.join(storage_path, "shared_keys.json")
        self.otp_file = os.path.join(storage_path, "otp_keys.json")
        os.makedirs(storage_path, exist_ok=True)
        self._initialize_files()

    def _initialize_files(self):
        """Create empty files if they don’t exist."""
        for file in [self.vigenere_file, self.otp_file]:
            if not os.path.exists(file):
                with open(file, 'w') as f:
                    json.dump({"version": "1.0", "keys": {}}, f, indent=2)

    def load_keys(self, cipher_type):
        """Load saved keys depending on cipher type."""
        file = self.vigenere_file if cipher_type.lower() == "vigenere" else self.otp_file
        with open(file, 'r') as f:
            return json.load(f).get("keys", {})

    def save_key(self, cipher_type, key_id, key_value):
        """Save new key entry with timestamp."""
        file = self.vigenere_file if cipher_type.lower() == "vigenere" else self.otp_file
        if os.path.exists(file):
            with open(file, 'r') as f:
                data = json.load(f)
        else:
            data = {"version": "1.0", "keys": {}}

        data["keys"][key_id] = {
            "key_value": key_value,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }

        with open(file, 'w') as f:
            json.dump(data, f, indent=2)

    def key_exists(self, cipher_type, key_value):
        """Check if key already exists in storage."""
        keys = self.load_keys(cipher_type)
        return any(entry["key_value"] == key_value for entry in keys.values())


if __name__ == "__main__":
    store = KeyStorage()
    print("=== CipherSafe Key Storage Demo ===")

    # Example: save sample keys
    store.save_key("vigenere", "EP1_START", "STEALTH")
    store.save_key("otp", "EP3_KEY", "YHPLQRMZTAX")

    print("Vigenère Keys:", store.load_keys("vigenere"))
    print("OTP Keys:", store.load_keys("otp"))
