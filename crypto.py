from Crypto.Cipher import AES 
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Protocol.KDF import PBKDF2
import os
import struct

def encrypt(plaintext, password):
    salt = os.urandom(16)
    iterations = 10000  # or random.randint(1000, 20000)
    key = PBKDF2(password, salt, dkLen=32, count=iterations)
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(plaintext.encode(), 16)
    ciphertext = cipher.encrypt(padded_data)
    # Pack: [salt (16)] [iterations (4)] [iv (16)] [ciphertext] packed all the info needed in one bytes object
    packed = salt + struct.pack('>I', iterations) + iv + ciphertext
    return packed

def decrypt(packed, password):
    salt = packed[:16]
    iterations = struct.unpack('>I', packed[16:20])[0]
    iv = packed[20:36]
    ciphertext = packed[36:]
    key = PBKDF2(password, salt, dkLen=32, count=iterations)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_plaintext = cipher.decrypt(ciphertext)
    return unpad(padded_plaintext, 16).decode('utf-8')



