import hashlib
from Crypto.Hash import MD2, MD4
from hashlib import md5 


class CryptographerMD2:
    def __init__(self):
        pass
    
    def encrypt(self, plain_text):
        if type(plain_text) == str:
            plain_text = plain_text.encode('utf-8')
        
        cipher = MD2.new(plain_text)
        cipher_text = cipher.hexdigest()
        return cipher_text

class CryptographerMD4:
    def __init__(self):
        pass
    
    def encrypt(self, plain_text):
        if type(plain_text) == str:
            plain_text = plain_text.encode('utf-8')
        
        cipher = MD4.new(plain_text)
        cipher_text = cipher.hexdigest()
        return cipher_text

class CryptographerMD5:
    def __init__(self):
        pass
    
    def encrypt(self, plain_text):
        if type(plain_text) == str:
            plain_text = plain_text.encode('utf-8')
        
        cipher = md5(plain_text)
        cipher_text = cipher.hexdigest()
        return cipher_text

class CryptographerRIPEMD:
    def __init__(self):
        pass
    
    def encrypt(self, plain_text):
        if type(plain_text) == str:
            plain_text = plain_text.encode('utf-8')
        
        cipher = hashlib.new('ripemd160')
        cipher.update(plain_text)
        cipher_text = cipher.hexdigest()
        return cipher_text

class CryptographerWHIRLPOOL:
    def __init__(self):
        pass
    
    def encrypt(self, plain_text):
        if type(plain_text) == str:
            plain_text = plain_text.encode('utf-8')
        
        cipher = hashlib.new('whirlpool')
        cipher.update(plain_text)
        cipher_text = cipher.hexdigest()
        return cipher_text
   
class CryptographerSHA1():
  
  def __init__(self):
    pass
  
  def encrypt(self,plain_text):
    if type(plain_text) == str:
      plain_text = plain_text.encode('utf-8')
      msg = hashlib.sha1(plain_text)
      return (msg.hexdigest())

      
class CryptographerSHA224():
  
  def __init__(self):
    pass
  
  def encrypt(self,plain_text):
    if type(plain_text) == str:
      plain_text = plain_text.encode('utf-8')
      msg = hashlib.sha224(plain_text)
      return (msg.hexdigest())
      
      
class CryptographerSHA256():
  
  def __init__(self):
    pass
  
  def encrypt(self,plain_text):
    is_string = False
    if type(plain_text) == str:
      plain_text = plain_text.encode('utf-8')
      msg = hashlib.sha256(plain_text)
      return (msg.hexdigest())
      
      
class CryptographerSHA384():
  
  def __init__(self):
    pass
  
  def encrypt(self,plain_text):
    if type(plain_text) == str:
      plain_text = plain_text.encode('utf-8')
      msg = hashlib.sha384(plain_text)
      return (msg.hexdigest())
      
      
class CryptographerSHA512():
  
  def __init__(self):
    pass
  
  def encrypt(self,plain_text):
    if type(plain_text) == str:
      plain_text = plain_text.encode('utf-8')
      msg = hashlib.sha512(plain_text)
      return (msg.hexdigest())
      
    
    
if __name__ == "__main__":

    plain_text = 'Bidisha2306'
    encrypted1 = CryptographerSHA1().encrypt(plain_text=plain_text)
    print(encrypted1)
    encrypted2 = CryptographerSHA224().encrypt(plain_text=plain_text)
    print(encrypted2)
    encrypted3 = CryptographerSHA256().encrypt(plain_text=plain_text)
    print(encrypted3)
    encrypted4 = CryptographerSHA384().encrypt(plain_text=plain_text)
    print(encrypted4)
    encrypted5 = CryptographerSHA512().encrypt(plain_text=plain_text)
    print(encrypted5)    
    print(hashlib.algorithms_available)
    print(CryptographerWHIRLPOOL().encrypt("Shouvik"))