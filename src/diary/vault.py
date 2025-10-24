"""
CipherSafe Diary Vault (vault.py)
---------------------------------
Stores and retrieves encrypted and decrypted messages.
Acts as the local “agent’s diary,” logging every communication.
"""

import json
import os
from datetime import datetime

from src.diary.message import Message


class DiaryVault:
    """
    Manages message storage, retrieval, and updates.
    Handles maintaining encrypted-to-decrypted message pairs in local JSON.
    """

    def __init__(self, vault_path="data/diary_vault.json"):
        self.vault_path = vault_path
        os.makedirs(os.path.dirname(vault_path), exist_ok=True)
        self._initialize_vault()

    def _initialize_vault(self):
        """Ensure JSON vault file exists."""
        if not os.path.exists(self.vault_path):
            with open(self.vault_path, 'w') as f:
                json.dump({"version": "1.0", "messages": []}, f, indent=2)

    def _load_vault(self):
        """Load vault JSON data."""
        with open(self.vault_path, 'r') as f:
            return json.load(f)

    def _save_vault(self, data):
        """Rewrite vault content safely."""
        with open(self.vault_path, 'w') as f:
            json.dump(data, f, indent=2)

    def add_entry(self, sender, receiver, cipher_type, ciphertext, plaintext=None, key_used=None):
        """
        Add new encrypted or decrypted message to vault.

        Args:
            sender (str): Message sender.
            receiver (str): Message recipient.
            cipher_type (str): Cipher type (Vigenère or Vernam).
            ciphertext (str): Encrypted message text.
            plaintext (str, optional): Decrypted text.
            key_used (str, optional): Encryption key used.
        """
        vault = self._load_vault()
        message = Message(sender, receiver, cipher_type, ciphertext, plaintext, key_used)
        vault["messages"].append(message.to_dict())
        self._save_vault(vault)
        return message.id

    def list_all(self):
        """Return all stored diary entries."""
        return self._load_vault()["messages"]

    def list_encrypted_only(self):
        """Return only encrypted (undecrypted) messages."""
        return [m for m in self._load_vault()["messages"] if m["status"] == "encrypted"]

    def update_entry(self, message_id, plaintext):
        """
        Update existing message with decrypted content.

        Args:
            message_id (str): UUID of stored message.
            plaintext (str): Decrypted text to store.
        """
        vault = self._load_vault()
        for msg in vault["messages"]:
            if msg["id"] == message_id:
                msg["plaintext"] = plaintext
                msg["status"] = "decrypted"
                msg["updated"] = datetime.utcnow().isoformat() + "Z"
                break
        self._save_vault(vault)
        return True

    def get_entry(self, message_id):
        """Retrieve a specific message by ID."""
        for msg in self._load_vault()["messages"]:
            if msg["id"] == message_id:
                return msg
        return None


# ---------------------
# Demo Usage
# ---------------------
if __name__ == "__main__":
    vault = DiaryVault()
    print("=== CipherSafe Diary Vault Demo ===")

    msg_id = vault.add_entry("ZOE", "MISATO", "Vigenère", "XKZFP", None, "STEALTH")
    print(f"Message added: {msg_id}")

    all_msgs = vault.list_all()
    print("All Entries:", all_msgs)

    vault.update_entry(msg_id, "HELLO AGENT")
    print("Updated Entry:", vault.get_entry(msg_id))
