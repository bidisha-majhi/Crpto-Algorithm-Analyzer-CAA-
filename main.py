from algorithms.symmetric_algorithms import CryptographerAES
from algorithms.hash_functions import *
from utils.consumption import ConsumptionMeasure

if __name__ == "__main__":
    consumption_measure = ConsumptionMeasure()
    crypt_obj = CryptographerAES(256)
    print("ENCRYPTION")
    with open('data/original/attempt1.txt', 'rb') as f:
        encrypted = consumption_measure.measure(
            lambda: crypt_obj.encrypt(f.read(), "shouvik"),
            epoch=1
        )
        with open('data/encrypted/encrypted.txt', 'wb') as e:
            e.write(encrypted)
    print("Energy Consumption (in micro Joules)", consumption_measure.get_energy_consumption())
    print("Time Taken (in microseconds)", consumption_measure.get_duration())

    print("\n\nDECRYPTION")
    with open('data/encrypted/encrypted.txt', 'rb') as e:
        decrypted = consumption_measure.measure(
            lambda: crypt_obj.decrypt(e.read(), "shouvik"),
            epoch=1
        )
        with open('data/decrypted/decrypted.txt', 'wb') as d:
            d.write(decrypted)
    print("Energy Consumption (in micro Joules)", consumption_measure.get_energy_consumption())
    print("Time Taken (in microseconds)", consumption_measure.get_duration())

    a = open('data/original/attempt1.txt', 'rb').read()
    b = open('data/decrypted/decrypted.txt', 'rb').read()
    from hashlib import sha1
    print(sha1(a).hexdigest() == sha1(b).hexdigest())