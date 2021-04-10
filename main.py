from algorithms.symmetric_algorithms import CryptographerAES


if __name__ == "__main__":
    aes_obj = CryptographerAES(256)
    with open('data/original/someText.txt', 'rb') as f: 
        encrypted = aes_obj.encrypt(f.read(), "shouvik")
        with open('data/encrypted/encrypted.txt', 'wb') as e:
            e.write(encrypted)
    with open('data/encrypted/encrypted.txt', 'rb') as e:
        decrypted = aes_obj.decrypt(e.read(), "shouvik")
        with open('data/decrypted/decrypted.txt', 'wb') as d:
            d.write(decrypted)