from Crypto.Cipher import AES, Blowfish
from Crypto import Random
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from struct import pack
from base64 import b64encode, b64decode
from hashlib import sha1, sha256
from twofish import Twofish


class CryptographerAES:

    def __init__(self, type: int=128):
        self.mode = AES.MODE_CBC
        self.type = type
    
    def create_key(self, secret: str):
        key = pad(secret.encode('utf-8'), 32).decode()
        if self.type == 128:
         
            return key[0:16]
        elif self.type == 256:
           
            return key[0:32]


    def encrypt(self, plain_text, secret: str):
        key = self.create_key(secret)
        is_string = False
        if type(plain_text) == str:
            is_string = True
            plain_text = plain_text.encode('utf-8')
        
        plain_text = pad(plain_text, AES.block_size)

        key = key.encode('utf-8')
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

        key = key.encode('utf-8')
        cipher = AES.new(key, self.mode, iv)
        plain_text = cipher.decrypt(cipher_text)
        plain_text = unpad(plain_text, AES.block_size)
        return plain_text.decode() if is_string else plain_text
    

class CryptographerBlowfish:
    def __init__(self):
        self.mode = Blowfish.MODE_CBC

    def create_key(self, secret: str):
        if len(secret)<4:
            key = pad(secret.encode('utf-8'), 4).decode()
        elif len(secret)<=56:
            key = secret
        else:
            key = secret[0:56]
        
        key = key.encode('utf-8')
        return key
  
    def encrypt(self, plain_text, secret:str):
        bs = Blowfish.block_size

        is_string = False
        if type(plain_text) == str:
            plain_text= plain_text.encode('utf-8')
            is_string = True

        key = self.create_key(secret)

        iv = Random.new().read(bs)
        cipher = Blowfish.new(key, self.mode, iv)
        plen = bs - divmod(len(plain_text),bs)[1]
        padding = [plen]*plen
        padding = pack('b'*plen, *padding)
        msg = iv + cipher.encrypt(plain_text+padding)
        msg = b64encode(msg)
        return msg.decode() if is_string else msg

    def decrypt(self,cipher_text,secret:str):
        bs = Blowfish.block_size

        is_string = False
        if type(cipher_text) ==str:
            cipher_text=cipher_text.encode('utf-8')
            is_string = True

        key = self.create_key(secret)

        cipher_text = b64decode(cipher_text)
        iv = cipher_text[:bs]
        cipher_text = cipher_text[bs:]
        cipher = Blowfish.new(key, self.mode, iv)
        msg = cipher.decrypt(cipher_text)
        last_byte = msg[-1]
        msg = msg[:- (last_byte if type(last_byte) is int else ord(last_byte))]
        return msg.decode() if is_string else msg


class CryptographerTwofish:

    def __init__(self):
        pass

    def create_key(self, secret:str):
        secret = secret if len(secret) <=30 else secret[0:30]
        key = "*" + secret + "*"
        
        return key

    def encrypt(self, plain_text, secret):
        key = self.create_key(secret)

        is_string = False
        if type(plain_text) == str:
            is_string = True
            plain_text = plain_text.encode('utf-8')

        plain_text = pad(plain_text, 16)

        key = key.encode('utf-8')
        
        cipher = Twofish(key)
        cipher_text = b""
        for i in range(0, len(plain_text), 16):
            plain_text_substring = plain_text[i: i+16]
            cipher_text_substring = cipher.encrypt(plain_text_substring)
            cipher_text_substring = b64encode(cipher_text_substring)
            cipher_text += cipher_text_substring
        
        return cipher_text.decode() if is_string else cipher_text

    def decrypt(self, cipher_text, secret):
        key = self.create_key(secret)
        is_string = False
        if type(cipher_text) == str:
            is_string = True
            cipher_text = cipher_text.encode('utf-8')
        
        key = key.encode('utf-8')
        
        cipher = Twofish(key)
        plain_text = b""
        for i in range(0, len(cipher_text), 24):
            cipher_text_substring = b64decode(cipher_text[i:i+24])
            plain_text += cipher.decrypt(cipher_text_substring)
        
        plain_text = unpad(plain_text, 16)
        
        return plain_text.decode() if is_string else plain_text

if __name__ == "__main__":
    c = CryptographerBlowfish()
    plain_text  = "Hello World "*5
    encrypted = c.encrypt(plain_text=plain_text, secret='shouvik')
    print(encrypted)
    decrypted = c.decrypt(cipher_text=encrypted, secret='shouvik')
    print(decrypted)
    
