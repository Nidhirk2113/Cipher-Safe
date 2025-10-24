"""
CipherSafe: Spy Diary Encryption System
--------------------------------------
Main Application File (main.py)

Manages user interaction with the diary system, encryption modules,
key management, and storyline progression in a spy-themed interface.
"""

from src.ciphers.vigenere import VigenereCipher
from src.ciphers.vernam import VernamCipher
from src.key_management.otp_manager import OTPKeyManager
from src.diary.vault import DiaryVault
from src.story.episodes import EpisodeManager
import json
import sys
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\nPress Enter to continue...")

def main_menu():
    print("=" * 60)
    print("        CIPHER-SAFE: SPY DIARY ENCRYPTION SYSTEM")
    print("=" * 60)
    print("1. Write New Message")
    print("2. Decrypt Received Message")
    print("3. View Diary Vault")
    print("4. Continue Story")
    print("5. Exit")
    print("=" * 60)
    return input("Select an option: ")

def write_new_message(vault, vigenere, vernam, otp_manager):
    clear_screen()
    print("WRITE NEW MESSAGE\n")
    message = input("Enter your message: ").upper().strip()
    recipient = input("Recipient (e.g. MISATO): ").upper().strip()
    mode = input("Encryption Mode [1=Vigenère, 2=Vernam OTP]: ")

    if mode == "1":
        keyword = input("Enter shared keyword (Vigenère): ").upper().strip()
        ciphertext = vigenere.encrypt(message, keyword)
        cipher_type = "Vigenère"
        key_used = keyword

    elif mode == "2":
        otp_key = otp_manager.get_new_key(len(message))
        ciphertext, key_used = vernam.encrypt(message, otp_key)
        otp_manager.mark_key_used(key_used)
        cipher_type = "Vernam OTP"

        # Optional Steganography (future enhancement)
        use_steg = input("Embed in image using steganography? (y/n): ").lower()
        if use_steg == 'y':
            print("[info] Placeholder for steganography embedding...")

    else:
        print("Invalid mode.")
        return

    vault.add_entry(sender="ZOE", receiver=recipient, cipher_type=cipher_type,
                    ciphertext=ciphertext, plaintext=message, key_used=key_used)
    print(f"\nMessage encrypted with {cipher_type}.")
    print(f"Ciphertext: {ciphertext}")
    pause()

def decrypt_message(vault, vigenere, vernam, otp_manager):
    clear_screen()
    print("DECRYPT RECEIVED MESSAGE\n")
    messages = vault.list_encrypted_only()
    if not messages:
        print("No encrypted messages found.")
        pause()
        return

    for i, msg in enumerate(messages, 1):
        print(f"{i}. {msg['cipher_type']} | From {msg['sender']}")

    choice = int(input("Select a message to decrypt: ")) - 1
    msg = messages[choice]

    if msg['cipher_type'] == "Vigenère":
        keyword = input("Enter shared keyword: ").upper().strip()
        plaintext = vigenere.decrypt(msg['ciphertext'], keyword)
    elif msg['cipher_type'] == "Vernam OTP":
        otp_key = input("Enter OTP key: ").upper().strip()
        if otp_manager.is_key_used(otp_key):
            print("This OTP key has already been used and is invalid!")
            pause()
            return
        plaintext = vernam.decrypt(msg['ciphertext'], otp_key)
        otp_manager.mark_key_used(otp_key)
    else:
        print("Unsupported cipher type.")
        return

    print(f"\nDecrypted Message: {plaintext}")
    vault.update_entry(msg['id'], plaintext)
    pause()

def view_diary(vault):
    clear_screen()
    entries = vault.list_all()
    if not entries:
        print("The diary vault is empty.")
    else:
        for e in entries:
            print(f"ID: {e['id']} | Type: {e['cipher_type']}")
            print(f"From: {e['sender']} → To: {e['receiver']}")
            print(f"Cipher: {e['ciphertext']}")
            if 'plaintext' in e:
                print(f"Decrypted: {e['plaintext']}")
            print("-" * 60)
    pause()

def continue_story(episodes):
    clear_screen()
    print("CONTINUE STORY\n")
    episodes.show_progress()
    next_episode = episodes.unlock_next()
    if next_episode:
        print(f"\nNew Episode Unlocked: {next_episode['title']}")
        print(next_episode['description'])
    else:
        print("All episodes completed!")
    pause()

def main():
    clear_screen()
    vigenere = VigenereCipher()
    vernam = VernamCipher()
    otp_manager = OTPKeyManager()
    vault = DiaryVault()
    episodes = EpisodeManager()

    while True:
        choice = main_menu()
        if choice == "1":
            write_new_message(vault, vigenere, vernam, otp_manager)
        elif choice == "2":
            decrypt_message(vault, vigenere, vernam, otp_manager)
        elif choice == "3":
            view_diary(vault)
        elif choice == "4":
            continue_story(episodes)
        elif choice == "5":
            print("Exiting CipherSafe. Goodbye, Agent ZOE.")
            sys.exit()
        else:
            print("Invalid option.")
            pause()

if __name__ == "__main__":
    main()
