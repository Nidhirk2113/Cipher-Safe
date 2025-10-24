# CipherSafe: Spy Diary Encryption System

### A Spy-Themed Secure Messaging and Cryptography Learning Project

CipherSafe is a Python-based educational project that combines **cryptography**, **steganography**, and **interactive storytelling**.  
It simulates encrypted communications between fictional spies while teaching encryption, key management, and digital secrecy concepts.

---

## 🎯 Objectives

- Implement **Vigenère** and **Vernam (One-Time Pad)** ciphers.
- Demonstrate **secure message exchange** and **key lifecycle enforcement**.
- Introduce **steganography** for covert data hiding.
- Enable **story-driven progression** through five spy missions.
- Showcase cryptographic best practices using Python.

---

## 🧱 Architecture Overview

CipherSafe is composed of modular layers:

| Layer | Modules | Description |
|-------|----------|-------------|
| **Cipher Core** | `vigenere.py`, `vernam.py`, `cipher_base.py` | Implements encryption/decryption logic |
| **Key Management** | `key_generator.py`, `otp_manager.py`, `key_storage.py` | Handles secure, trackable keys |
| **Messaging System** | `message.py`, `vault.py` | Logs and manages encrypted diary entries |
| **Steganography** | `lsb_stego.py` | Hides ciphertext inside images (optional) |
| **Story Engine** | `characters.py`, `episodes.py`, `narrative.py` | Interactive espionage storyline |
| **Interface** | `cli.py`, `menu.py`, `main.py` | User-facing terminal interaction |

---

## 🧩 Features

- Encrypt/decrypt using **Vigenère Cipher (polyalphabetic)**  
- Generate and enforce single-use **Vernam OTP keys**  
- Embed ciphertext into images using **LSB Steganography**  
- Log communications in a **secure diary JSON vault**  
- Progress through **five spy missions** connected to cryptographic lessons  

---

## 🕹️ Usage

### 1. Installation
Ensure Python 3.8+ is installed.

Then install dependencies:

pip install -r requirements.txt


### 2. Run CipherSafe
Launch the interactive terminal:
python main.py

or directly:
python -m ui.cli


### 3. Run Tests
To verify correct function:
pytest tests/ -v


---

## 🧠 Learning Outcomes

| Concept | Description |
|----------|-------------|
| **Symmetric Cryptography** | Learn how shared-key encryption works |
| **Classical vs Perfect Ciphers** | Compare Vigenère and One-Time Pad systems |
| **Steganography** | Hide text in image pixels |
| **Key Management** | Generate, store, and enforce one-time usage of keys |
| **Narrative Design** | Engage learners through story mechanics |

---

## 📁 Folder Structure

CipherSafe/
├── src/
│ ├── ciphers/ # Encryption logic (Vigenère, Vernam)
│ ├── steganography/ # Image-based hiding
│ ├── key_management/ # Key lifecycle management
│ ├── diary/ # Encrypted diary vault
│ ├── story/ # Characters & missions
│ └── ui/ # Command-line interface
│
├── data/ # Local storage
│ ├── diary_vault.json
│ ├── keys/
│ └── episodes/
│
├── docs/ # Educational resources
├── tests/ # Unit tests
└── main.py # Entry point



---

## 📚 Documentation

See the `/docs` folder for:
- **architecture.md** – Technical structure  
- **cipher_guide.md** – Cryptography guide  
- **storyline.md** – Spy mission summary  
- **implementation_guide.md** – Setup and integration  

---

## ⚠️ Security Disclaimer

CipherSafe is designed **for educational purposes only**.  
It is **not suitable** for real-world secure communication or data protection.

For production cryptography, use industry-standard libraries like:
- [`cryptography`](https://cryptography.io)
- [`PyCryptodome`](https://pycryptodome.readthedocs.io)

---

## 🏁 Credits

**Developed by:** Perplexity AI Labs (Educational Engineering Initiative)  
**License:** MIT  
**Version:** 1.0.0
