"""
CipherSafe Message Class (message.py)
-------------------------------------
Defines the structure of encrypted/decrypted messages exchanged between agents.
Each message entry is recorded within the Diary Vault with metadata such as
sender, receiver, timestamp, cipher type, and key reference.
"""

from datetime import datetime
import uuid

class Message:
    """
    Represents a single encrypted or decrypted communication entry.
    Used by DiaryVault for storage and retrieval operations.
    """

    def __init__(self, sender, receiver, cipher_type, ciphertext, plaintext=None, key_used=None):
        """
        Initialize a message entry.

        Args:
            sender (str): Name or code of sender (e.g., ZOE, MISATO)
            receiver (str): Recipient identifier
            cipher_type (str): Encryption method used
            ciphertext (str): Encrypted message text
            plaintext (str): Decrypted version of message (optional)
            key_used (str): Encryption key or reference (optional)
        """
        self.id = str(uuid.uuid4())
        self.sender = sender
        self.receiver = receiver
        self.cipher_type = cipher_type
        self.ciphertext = ciphertext
        self.plaintext = plaintext
        self.key_used = key_used
        self.timestamp = datetime.utcnow().isoformat() + "Z"
        self.status = "decrypted" if plaintext else "encrypted"

    def to_dict(self):
        """
        Convert message object to dictionary for JSON serialization.
        """
        return {
            "id": self.id,
            "sender": self.sender,
            "receiver": self.receiver,
            "cipher_type": self.cipher_type,
            "ciphertext": self.ciphertext,
            "plaintext": self.plaintext,
            "key_used": self.key_used,
            "timestamp": self.timestamp,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data):
        """
        Create a Message object from stored dictionary data.

        Args:
            data (dict): Serialized message dictionary.

        Returns:
            Message: Reconstructed message object.
        """
        msg = Message(
            data["sender"],
            data["receiver"],
            data["cipher_type"],
            data["ciphertext"],
            data.get("plaintext"),
            data.get("key_used")
        )
        msg.id = data.get("id", str(uuid.uuid4()))
        msg.timestamp = data.get("timestamp", datetime.utcnow().isoformat() + "Z")
        msg.status = data.get("status", "encrypted")
        return msg
