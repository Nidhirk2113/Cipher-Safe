# CipherSafe System Architecture

## Overview
CipherSafe is built on a modular architecture designed for clarity, reusability, and educational value.  
Each component is isolated by function: encryption logic, key management, messaging, steganography, UI, and story narrative.

---

## Core Architectural Layers

### 1. Cipher Layer
**Modules:** `vigenere.py`, `vernam.py`, `cipher_base.py`  
Implements both classical and perfect ciphers.  
Provides a standardized interface using `CipherBase`.

**Responsibilities:**
- Perform encryption/decryption transformations.
- Maintain educational transparency (no external crypto libraries).
- Demonstrate the contrast between breakable and unbreakable systems.

---

### 2. Key Management Layer
**Modules:** `key_generator.py`, `otp_manager.py`, `key_storage.py`  
Ensures secure, traceable, and single-use key handling.

**Responsibilities:**
- Use truly random keys (via `secrets`).
- Track and prevent OTP key reuse.
- Store and version keys safely in JSON files.

---

### 3. Messaging Layer
**Modules:** `message.py`, `vault.py`  
Acts as the “secure diary.” Handles message metadata, persistence, and version control.

**Responsibilities:**
- Store encrypted and decrypted message entries.
- Maintain consistent JSON structure for audit and retrieval.
- Enable cross-session data persistence using local storage.

---

### 4. Steganography Layer
**Module:** `lsb_stego.py`  
Provides covert communication through LSB image embedding.

**Responsibilities:**
- Hide Vernam ciphertext inside image pixel values.
- Support extraction for decryption.
- Integrate optional steg layer for critical mission episodes.

---

### 5. Story Layer
**Modules:** `characters.py`, `episodes.py`, `narrative.py`  
Drives story-based content progression, binding cryptographic actions with narrative context.

**Responsibilities:**
- Manage mission episodes and progress tracking.
- Relate each cryptographic concept to real-world threat escalation.
- Present learning outcomes through dialogue and interaction.

---

### 6. User Interface Layer
**Modules:** `cli.py`, `menu.py`, `main.py`  
Handles all terminal interactions and controls story-driven flow logic.

**Responsibilities:**
- Expose main user options (Encrypt, Decrypt, Vault, Story).
- Integrate storytelling with educational cryptography exercises.
- Provide immersive spy-themed CLI interface.

---

## Data Management
**Files:**  
- `diary_vault.json` — Message persistence  
- `shared_keys.json`, `otp_keys.json` — Key data  
- Human-readable, versioned for educational visibility.

---

## System Diagram

User
│
▼
CLI/Menu ───────────────► Narrative Controller
│ │
▼ ▼
Encrypt/Decrypt Story Progression
│ │
▼ ▼
Ciphers ◄─► Key Manager ─► Diary Vault
│
▼
Steganography (optional)


Each arrow represents data flow during encryption, decryption, and story progression.

---

## Design Goals
- **Clarity:** Modular and readable for students.
- **Demonstration:** Show real cryptographic principles.
- **Narrative Learning:** Reinforce theory through storytelling.
