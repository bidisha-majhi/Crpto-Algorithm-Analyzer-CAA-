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
    

class CryptographerBlowfish:
      
  
  def __init__(self):
    pass
  
  def encrypt(self, plaintext, key:str):
    bs = Blowfish.block_size
    isString = False
    if type(plaintext) ==str:
      plaintext= plaintext.encode('utf-8')
      isString = True
    key = sha1(key.encode()).hexdigest().encode('utf-8')
    iv = Random.new().read(bs)
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    plen = bs - divmod(len(plaintext),bs)[1]
    padding = [plen]*plen
    padding = pack('b'*plen, *padding)
    msg = iv + cipher.encrypt(plaintext+padding)
    msg = b64encode(msg)
    return msg.decode() if isString else msg
    
    
      
  def decrypt(self,ciphertext,key:str):
    bs = Blowfish.block_size
    isString = False
    if type(ciphertext) ==str:
      ciphertext=ciphertext.encode('utf-8')
      isString = True
    key = sha1(key.encode()).hexdigest().encode('utf-8')
    ciphertext = b64decode(ciphertext)
    iv = ciphertext[:bs]
    ciphertext = ciphertext[bs:]
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    msg = cipher.decrypt(ciphertext)
    last_byte = msg[-1]
    msg = msg[:- (last_byte if type(last_byte) is int else ord(last_byte))]
    return msg.decode() if isString else msg

    
    


class CryptographerTwofish:
    
    def __init__(self):
        pass

    def create_key(self, secret:str):
        key = sha1(secret.encode()).hexdigest()
        key = key[:30]
        return key

    def encrypt(self, plain_text, secret):
        secret = "*"+self.create_key(secret)+"*"

        is_string = False
        if type(plain_text) == str:
            is_string = True
            plain_text = plain_text.encode('utf-8')

        plain_text = pad(plain_text, 16)

        secret = secret.encode('utf-8')
        
        cipher = Twofish(secret)
        cipher_text = b""
        for i in range(0, len(plain_text), 16):
            plain_text_substring = plain_text[i: i+16]
            cipher_text_substring = cipher.encrypt(plain_text_substring)
            cipher_text_substring = b64encode(cipher_text_substring)
            cipher_text += cipher_text_substring
       
        return cipher_text.decode() if is_string else cipher_text

    def decrypt(self, cipher_text, secret):
        secret = "*"+self.create_key(secret)+"*"
        is_string = False
        if type(cipher_text) == str:
            is_string = True
            cipher_text = cipher_text.encode('utf-8')
        
        secret = secret.encode('utf-8')
        
        cipher = Twofish(secret)
        plain_text = b""
        for i in range(0, len(cipher_text), 24):
            cipher_text_substring = b64decode(cipher_text[i:i+24])
            plain_text += cipher.decrypt(cipher_text_substring)
        
        plain_text = unpad(plain_text, 16)
        
        return plain_text.decode() if is_string else plain_text

if __name__ == "__main__":
    c = CryptographerTwofish()
    plain_text  = "Hello World "*5
    encrypted = CryptographerTwofish().encrypt(plain_text=plain_text, secret='shouvikshouvikshouvikshouviksh')
    print(encrypted)
    decrypted = CryptographerTwofish().decrypt(cipher_text=encrypted, secret='shouvikshouvikshouvikshouviksh')
    print(decrypted)
