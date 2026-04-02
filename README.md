# Multiplicative Cipher + Rotating Hash

**Cipher assigned:** Multiplicative Cipher (Roll no. mod 10 = 2)  
**Language:** Python 3  
**Hash chosen:** Rotating Hash — implemented from scratch

---

## Files

| File | Description |
|------|-------------|
| `main.py` | Multiplicative Cipher (encrypt + decrypt) with user input, imports hash |
| `hash_function.py` | Rotating hash implemented from scratch |
| `test_roundtrip.py` | Full encrypt → hash → decrypt test script |

---

## Multiplicative Cipher - Theory

The multiplicative cipher is a substitution cipher where each plaintext letter is multiplied by a key value modulo 26 to get the ciphertext letter.

**Encryption:**
```
C = (P * key) mod 26
```

**Decryption:**
```
P = (C * key_inverse) mod 26
```

Where P and C are alphabet positions (A=0 ... Z=25) and key_inverse is the modular multiplicative inverse of the key mod 26.

The key constraint is that the key must be **coprime with 26** (i.e. gcd(key, 26) = 1). If this condition is not met, multiple plaintext letters map to the same ciphertext letter, making decryption impossible. The valid keys are:

```
1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25
```

To decrypt, we need the modular inverse of the key. For example if key = 7, then key_inverse = 15 because (7 * 15) mod 26 = 1.

---

## Rotating Hash - Theory

The rotating hash uses bit rotation instead of bit shifting. Most simple hashes (like djb2 or sdbm) shift bits left, which means high bits eventually fall off and are lost. Rotation moves them to the other end instead so no information is discarded.

**Formula for each character:**
```
hash = rotate_left(hash, 4) XOR char
```

**Rotate left by 4 on a 32-bit value:**
```
rotl(hash, 4) = ((hash << 4) | (hash >> 28)) & 0xFFFFFFFF
```

The rotation amount of 4 bits means after 8 characters the hash has completed a full 32-bit cycle, giving good mixing especially for short strings. XOR with the character value then folds the new byte into the rotated hash.

I chose this hash because the rotation idea is genuinely different from all the multiply-and-add hashes most people implement, and I could understand exactly what each bit operation was doing.

---

## How to Run

Python 3, no external libraries needed.

```bash
python main.py           # interactive program + worked examples
python hash_function.py  # test hash standalone
python test_roundtrip.py # run all tests
```

---

## Worked Examples

### Example 1

| Field | Value |
|-------|-------|
| Plaintext | `HELLO` |
| Key | `7` |
| Ciphertext | `XCZZU` |
| Rotating Hash | `005c6ff5` |
| Decrypted | `HELLO` ✓ |

Manual check for first letter:
- H = 7, key = 7 → (7 * 7) mod 26 = 49 mod 26 = 23 → **X** ✓

### Example 2

| Field | Value |
|-------|-------|
| Plaintext | `NETWORKSECURITY` |
| Key | `11` |
| Ciphertext | `NSBIYFGQSWMFKBE` |
| Rotating Hash | `0d4fe247` |
| Decrypted | `NETWORKSECURITY` ✓ |

Manual check for first letter:
- N = 13, key = 11 → (13 * 11) mod 26 = 143 mod 26 = 13 → **N** ✓

---

## References

- Stinson, D.R. - Cryptography: Theory and Practice
- https://en.wikipedia.org/wiki/Multiplicative_cipher
- Rotating hash: https://en.wikipedia.org/wiki/Rolling_hash
