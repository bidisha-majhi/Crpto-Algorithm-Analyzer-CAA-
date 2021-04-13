from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
from hashlib import sha1, sha256
from twofish import Twofish


class CryptographerAES:

    def __init__(self, type: int=128):
        self.mode = AES.MODE_CBC
        if type == 128:
            self.key_hash_fn = sha1
        elif type == 256:
            self.key_hash_fn = sha256
    
    def create_key(self, secret: str):
        key = self.key_hash_fn(secret.encode()).digest()
        if self.key_hash_fn == sha1:
            return key[0:16]
        elif self.key_hash_fn == sha256:
            return key


    def encrypt(self, plain_text, secret: str):
        key = self.create_key(secret)
        is_string = False
        if type(plain_text) == str:
            is_string = True
            plain_text = plain_text.encode('utf-8')
        
        plain_text = pad(plain_text, AES.block_size)

        cipher = AES.new(key, self.mode)
        iv = cipher.iv

        cipher_text = cipher.encrypt(plain_text)

        cipher_text = b64encode(iv+cipher_text)

        return cipher_text.decode() if is_string else cipher_text
    
    def decrypt(self, cipher_text, secret: str):
        key = self.create_key(secret)
        is_string = False
        if type(cipher_text) == str:
            is_string = True
            cipher_text = cipher_text.encode('utf-8')
        cipher_text = b64decode(cipher_text)
        iv, cipher_text = cipher_text[:16], cipher_text[16:]
        cipher = AES.new(key, self.mode, iv)
        plain_text = cipher.decrypt(cipher_text)
        plain_text = unpad(plain_text, AES.block_size)
        return plain_text.decode() if is_string else plain_text


class CryptographerTwofish:
    
    def __init__(self):
        pass

    def encrypt(self, plain_text, secret: str):
        if type(plain_text) == str:
            is_string = True
            plain_text = plain_text.encode('utf-8')
        secret = secret.encode('utf-8')
        cipher = Twofish(secret)
        cipher_text = cipher.encrypt(plain_text)
        print(cipher_text)

    def decrypt(self, cipher_text, secret: str):
        if type(cipher_text) == str:
            is_string = True
            cipher_text = cipher_text.encode('utf-8')
        secret = secret.encode('utf-8')
        cipher = Twofish(secret)
        plain_text = cipher.decrypt(cipher_text)
        print(plain_text)