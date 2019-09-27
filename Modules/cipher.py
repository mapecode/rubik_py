import hashlib
from Crypto.Cipher import AES


def encode(s):
    h = hashlib.md5(s.encode())
    return h.hexdigest()

def decode(enc):



encode("pruebkjhjklhljljhjhohuhlkha")
encode("jj")
