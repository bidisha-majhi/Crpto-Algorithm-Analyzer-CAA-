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
