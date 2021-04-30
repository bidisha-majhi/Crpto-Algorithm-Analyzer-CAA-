from algorithms.symmetric_algorithms import *
from algorithms.hash_functions import *

if __name__ == "__main__":
    crypt_obj = CryptographerSHA512()
    with open('data/original/someText.txt', 'rb') as f:
        encrypted = crypt_obj.encrypt(f.read())
        #with open('data/encrypted/encrypted.txt', 'wb') as e:
            #e.write(encrypted)
        print(encrypted)

    '''
    with open('data/encrypted/encrypted.txt', 'rb') as e:
        decrypted = crypt_obj.decrypt(e.read(), "shouvik")
        with open('data/decrypted/decrypted.txt', 'wb') as d:
            d.write(decrypted)
    '''