import hashlib


def encode(s):
    h = hashlib.md5(s.encode())
    return h.hexdigest()

