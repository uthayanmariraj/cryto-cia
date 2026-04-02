# hash_function.py
# Rotating Hash - implemented from scratch
#
# I chose the Rotating hash because it uses bit rotation instead of
# just shifting, which means no bits are ever lost. Most simple hashes
# like djb2 or sdbm just shift bits left, so the high bits eventually
# fall off. Rotation moves them to the other end instead.
#
# Formula for each character:
#   hash = (hash rotated left by 4 bits) XOR char
#
# To rotate left by 4 on a 32-bit value:
#   rotl(hash, 4) = ((hash << 4) | (hash >> 28)) & 0xFFFFFFFF
#
# XORing with the character mixes the new byte into the hash.
# The rotation amount (4 bits) is chosen so that after 8 characters
# the hash has done a full cycle, giving good mixing for short strings.
# Output is a 32-bit value shown as 8 hex characters.

def rotate_left(val, n, bits=32):
    # rotate val left by n bits within a 'bits'-wide integer
    n = n % bits
    return ((val << n) | (val >> (bits - n))) & ((1 << bits) - 1)

def rotating_hash(text):
    if type(text) != str:
        text = str(text)

    hash_val = 0

    for ch in text:
        hash_val = rotate_left(hash_val, 4) ^ ord(ch)
        hash_val = hash_val & 0xFFFFFFFF

    return format(hash_val, '08x')


if __name__ == "__main__":
    print(rotating_hash("hello"))
    print(rotating_hash("HELLO"))
    print(rotating_hash("MULTIPLICATIVE"))
    print(rotating_hash(""))

    # avalanche check
    print(rotating_hash("abc"))
    print(rotating_hash("abd"))
