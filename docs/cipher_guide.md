# CipherSafe: Cryptographic Implementation Guide

## Vigenère Cipher

### Description
A polyalphabetic substitution cipher invented in the 16th century.  
Each letter of plaintext is shifted by an amount determined by the corresponding letter in a keyword.

### Example
Plaintext: ATTACKATDAWN  
Key: LEMON  
Ciphertext: LXFOPVEFRNHR

### Formula
\[
C_i = (P_i + K_i) \mod 26
\]
and
\[
P_i = (C_i - K_i + 26) \mod 26
\]

### Code Reference
`ciphers/vigenere.py`

---

## Vernam Cipher (One-Time Pad)

### Description
Developed in 1917, the Vernam cipher is truly unbreakable if used correctly.  
Each letter is XORed with a random key of the same length.

### Formula
\[
C_i = (P_i + K_i) \mod 26
\]
\[
P_i = (C_i - K_i + 26) \mod 26
\]

### Perfect Secrecy Conditions
1. Key is random.
2. Key length ≥ Message length.
3. Key is never reused.
4. Key remains secret.

### Code Reference
`ciphers/vernam.py`

---

## Comparison

| Feature | Vigenère | Vernam (OTP) |
|----------|-----------|--------------|
| Year | 1586 | 1917 |
| Type | Polyalphabetic substitution | Perfect secrecy symmetric cipher |
| Key | Repeating keyword | Random pad |
| Key Reuse | Allowed (less secure) | Never allowed |
| Breakability | Vulnerable to frequency analysis | Mathematically unbreakable |

---

## Steganography
**Module:** `lsb_stego.py`  
Hides Vernam ciphertext within the least significant bits of image pixels.

### Encoding Process
1. Convert plaintext to binary.
2. Replace least significant bits in image pixels with message bits.
3. Save image.

### Decoding Process
Reverse the steps and stop at pre-defined terminator sequence.

---

## Educational Objective
CipherSafe demonstrates:
- The historical evolution of encryption.
- Conceptual bridge from classical cryptography to modern methods.
- Practical application of key management and message security.
