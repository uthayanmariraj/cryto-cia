# Multiplicative Cipher in C++

## Overview
This project implements the Multiplicative Cipher, a classical encryption technique in cryptography. It allows users to encrypt and decrypt alphabetic text using a numeric key.

The cipher works by multiplying each letter's position in the alphabet by a key value modulo 26.

---

## Features
- Encrypts alphabetic text using a multiplicative key
- Decrypts text using the modular inverse of the key
- Preserves case (uppercase and lowercase letters)
- Leaves non-alphabet characters unchanged
- Validates key to ensure it is coprime with 26

---

## How It Works

### Encryption Formula
E(x) = (a * x) mod 26

### Decryption Formula
D(x) = (a⁻¹ * x) mod 26

Where:
- x = position of the letter (0–25)
- a = encryption key
- a⁻¹ = modular inverse of a under mod 26

---

## Requirements
- C++ compiler (e.g., g++, clang++)
- Standard C++ libraries

---

## Compilation and Execution

### Compile
g++ multiplicative_cipher.cpp -o cipher

### Run
./cipher

---

## Usage
1. Enter the plaintext message
2. Enter a key (must be coprime with 26)
3. The program will:
   - Encrypt the message
   - Decrypt it back to verify correctness

---

## Example
Enter text: HELLO  
Enter key (a): 5  

Encrypted: CZGGJ  
Decrypted: HELLO  

---

## Key Constraints
The key must satisfy:
gcd(a, 26) = 1

Valid keys include:
1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25

Invalid keys (e.g., 2, 4, 6, 13, etc.) will not work because they do not have a modular inverse.

---

## File Structure
multiplicative_cipher.cpp   # Main source code  
README.md                   # Documentation  

---

## Limitations
- Only works with English alphabets (A–Z, a–z)
- Uses brute-force method for modular inverse
- Not suitable for modern secure encryption

---

## Future Improvements
- Optimize modular inverse using Extended Euclidean Algorithm
- Add support for affine cipher
- Provide user option to choose encryption or decryption separately
- Improve UI/UX

---

## License
This project is open-source and free to use for educational purposes.
