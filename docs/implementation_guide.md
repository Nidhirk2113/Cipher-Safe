# CipherSafe Implementation Guide

## Setup

### Requirements
- Python 3.8+
- Pillow (`pip install Pillow`)
- pytest (for unit tests)
- colorama (optional, for styled CLI output)

### Folder Setup
Run:
    mkdir -p data/keys assets/images assets/stego_output tests

---

## Execution
Launch the system:
    python main.py

or through the CLI module:
    python -m ui.cli


---

## Testing
To ensure correctness:
    pytest tests/ -v


---

## Implementation Steps
1. Implement core ciphers (`vigenere.py`, `vernam.py`).
2. Create message vault (`vault.py`) and JSON storage.
3. Add key management (generation, storage, OTP enforcement).
4. Integrate story modules to control mission progression.
5. Link via main interface (CLI).

---

## Integration Notes
- Modular design allows easy scalability.
- JSON persistence makes system stateless between runs.
- Future addition: GUI using Tkinter or Flask.

---

## Security Caveats
CipherSafe is **educational** — not for real-world cryptography.
Keys are stored in plaintext for transparency.  
A production system would require key encryption, secure channels, and proper authentication.

---

## Learning Validation Checklist
✅ Encrypt & decrypt successfully  
✅ Use OTP only once  
✅ Extract hidden messages from image  
✅ Track missions as story unfolds  
✅ Run all tests successfully  

---

### End of Document
*CipherSafe — Educational cryptography meets interactive storytelling.*
