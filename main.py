# main.py
# Multiplicative Cipher - Encryption and Decryption
#
# The multiplicative cipher encrypts by multiplying each letter's position
# by a key value (mod 26). The key must be coprime with 26 (i.e. gcd(key,26)=1)
# otherwise some letters map to the same ciphertext letter and decryption
# becomes impossible.
#
# Valid keys (coprime with 26): 1,3,5,7,9,11,15,17,19,21,23,25

from hash_function import rotating_hash

# only these keys work - they must be coprime with 26
VALID_KEYS = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]


def gcd(a, b):
    # euclidean algorithm to find greatest common divisor
    while b != 0:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    # find x such that (a * x) mod m = 1
    # using extended euclidean algorithm
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def clean(text):
    out = ""
    for ch in text:
        if ch.isalpha():
            out += ch.upper()
    return out


def encrypt(plaintext, key):
    if gcd(key, 26) != 1:
        print(f"Error: key {key} is not coprime with 26. Valid keys: {VALID_KEYS}")
        return ""

    plain = clean(plaintext)
    result = ""
    for ch in plain:
        p = ord(ch) - ord('A')
        c = (p * key) % 26
        result += chr(c + ord('A'))
    return result


def decrypt(ciphertext, key):
    if gcd(key, 26) != 1:
        print(f"Error: key {key} is not coprime with 26. Valid keys: {VALID_KEYS}")
        return ""

    inv = mod_inverse(key, 26)
    if inv is None:
        print("Error: could not find modular inverse for this key")
        return ""

    cipher = clean(ciphertext)
    result = ""
    for ch in cipher:
        c = ord(ch) - ord('A')
        p = (c * inv) % 26
        result += chr(p + ord('A'))
    return result


def print_example(title, plaintext, key):
    plain = clean(plaintext)
    enc   = encrypt(plain, key)
    h     = rotating_hash(enc)
    dec   = decrypt(enc, key)
    print(f"\n{title}")
    print(f"  Plaintext     : {plain}")
    print(f"  Key           : {key}")
    print(f"  Ciphertext    : {enc}")
    print(f"  Rotating Hash : {h}")
    print(f"  Decrypted     : {dec}")


if __name__ == "__main__":
    print("=" * 50)
    print("       Multiplicative Cipher")
    print("=" * 50)
    print(f"\nValid keys (coprime with 26): {VALID_KEYS}")

    print_example("Example 1:", "HELLO", 7)
    print_example("Example 2:", "NETWORK SECURITY", 11)

    print("\n" + "=" * 50)
    print("         Encrypt / Decrypt")
    print("=" * 50)

    while True:
        print("\n1. Encrypt")
        print("2. Decrypt")
        print("3. Quit")
        choice = input("Choice: ").strip()

        if choice == "1":
            msg = input("Enter plaintext: ").strip()
            try:
                key = int(input(f"Enter key {VALID_KEYS}: ").strip())
            except ValueError:
                print("Key must be a number.")
                continue
            enc = encrypt(msg, key)
            if enc:
                print("Ciphertext    :", enc)
                print("Rotating Hash :", rotating_hash(enc))

        elif choice == "2":
            msg = input("Enter ciphertext: ").strip()
            try:
                key = int(input(f"Enter key {VALID_KEYS}: ").strip())
            except ValueError:
                print("Key must be a number.")
                continue
            dec = decrypt(msg, key)
            if dec:
                print("Plaintext  :", dec)

        elif choice == "3":
            break

        else:
            print("Invalid option, try again.")
