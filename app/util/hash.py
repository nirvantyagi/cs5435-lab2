from hashlib import sha256, pbkdf2_hmac
from random import getrandbits


# Generate 128-bit random salt as string of hex values
def random_salt():
    return getrandbits(128).to_bytes(16, byteorder='little').hex()


# Input: string; Output: string of hex values
def hash_sha256(x):
    return sha256(x.encode('utf-8')).hexdigest()


# Input: string x and string of hex salt; Output: string of hex values
def hash_pbkdf2(x, salt):
    return pbkdf2_hmac('sha256', x.encode('utf-8'), bytes.fromhex(salt), 100000).hex()

