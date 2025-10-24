"""
CipherSafe Command-Line Interface (cli.py)
------------------------------------------
Provides the interactive user interface for CipherSafe.
Manages main menu navigation, encryption/decryption, story progression,
and diary vault interaction.
"""

import sys
from ciphers.vigenere import VigenereCipher
from ciphers.vernam import VernamCipher
from key_management.otp_manager import OTPKeyManager
from diary.vault import DiaryVault
from story.narrative import NarrativeController
from ui.menu import Menu


class CipherSafeCLI:
    """Main command-line interface for CipherSafe system."""

    def __init__(self):
        self.vigenere = VigenereCipher()
        self.vernam = VernamCipher()
        self.otp_manager = OTPKeyManager()
        self.vault = DiaryVault()
        self.story = NarrativeController()

    # ---------------------------
    # Encryption / Decryption
    # ---------------------------

    def encrypt_message(self):
        print("\n=== ENCRYPT MESSAGE ===")
        message = input("Enter message to encrypt: ").upper()
        mode = input("Select cipher [1=Vigenère, 2=Vernam OTP]: ").strip()

        if mode == "1":
            keyword = input("Enter shared keyword for Vigenère: ").upper()
            ciphertext = self.vigenere.encrypt(message, keyword)
            print(f"\nCiphertext: {ciphertext}")
            self.vault.add_entry("ZOE", "MISATO", "Vigenère", ciphertext, message, keyword)
            print("Message added to vault.")

        elif mode == "2":
            otp_key = self.otp_manager.get_new_key(len(message))
            ciphertext, otp_generated = self.vernam.encrypt(message, otp_key)
            print(f"\nGenerated OTP Key: {otp_generated}")
            print(f"Ciphertext: {ciphertext}")
            self.otp_manager.mark_key_used(otp_generated)
            self.vault.add_entry("ZOE", "MISATO", "Vernam OTP", ciphertext, message, otp_generated)
            print("Message added to vault.")

        else:
            print("Invalid mode selected.")
        input("\nPress Enter to continue...")

    def decrypt_message(self):
        print("\n=== DECRYPT MESSAGE ===")
        entries = self.vault.list_encrypted_only()

        if not entries:
            print("No encrypted messages available.")
            input("Press Enter to return.")
            return

        for i, msg in enumerate(entries, start=1):
            print(f"{i}. {msg['cipher_type']} | From {msg['sender']} at {msg['timestamp']}")
        try:
            choice = int(input("Select message to decrypt: ")) - 1
            msg = entries[choice]
        except (ValueError, IndexError):
            print("Invalid selection.")
            return

        if msg['cipher_type'] == "Vigenère":
            keyword = input("Enter keyword for Vigenère: ").upper()
            plaintext = self.vigenere.decrypt(msg['ciphertext'], keyword)

        elif msg['cipher_type'] == "Vernam OTP":
            otp_key = input("Enter OTP key: ").upper()
            if self.otp_manager.is_key_used(otp_key):
                print("OTP key has already been used; cannot decrypt again!")
                return
            plaintext = self.vernam.decrypt(msg['ciphertext'], otp_key)
            self.otp_manager.mark_key_used(otp_key)

        else:
            print("Unsupported cipher.")
            return

        print(f"\nDecrypted Message: {plaintext}")
        self.vault.update_entry(msg['id'], plaintext)
        input("Press Enter to continue...")

    # ---------------------------
    # Storyline / Diary
    # ---------------------------

    def view_vault(self):
        print("\n=== DIARY VAULT ===")
        messages = self.vault.list_all()
        if not messages:
            print("No messages recorded yet.")
        else:
            for m in messages:
                print("-" * 60)
                print(f"{m['sender']} → {m['receiver']} ({m['cipher_type']})")
                print(f"Encrypted: {m['ciphertext']}")
                if m.get('plaintext'):
                    print(f"Decrypted: {m['plaintext']}")
                print(f"Timestamp: {m['timestamp']}")
        input("\nPress Enter to continue...")

    def continue_story(self):
        print("\n=== CONTINUE STORY ===")
        self.story.continue_story()
        input("\nPress Enter to return to Main Menu...")

    # ---------------------------
    # Main Application Loop
    # ---------------------------

    def run(self):
        main_menu = Menu("CIPHER-SAFE MAIN TERMINAL", [
            "Write/Encrypt New Message",
            "Decrypt Received Message",
            "View Diary Vault",
            "Continue Story",
            "Exit System"
        ])

        while True:
            choice = main_menu.get_choice()

            if choice == 1:
                self.encrypt_message()
            elif choice == 2:
                self.decrypt_message()
            elif choice == 3:
                self.view_vault()
            elif choice == 4:
                self.continue_story()
            elif choice == 5:
                print("Exiting CipherSafe terminal... stay encrypted, Agent.")
                sys.exit(0)


if __name__ == "__main__":
    app = CipherSafeCLI()
    app.run()
