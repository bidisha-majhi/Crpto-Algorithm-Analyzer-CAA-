from algorithms.symmetric_algorithms import CryptographerAES
from algorithms.hash_functions import *
from utils.consumption import ConsumptionMeasure

if __name__ == "__main__":
    consumption_measure = ConsumptionMeasure()
    crypt_obj = CryptographerAES(256)

    original_file = open("data/original/someText.txt", "rb").read()

    print("ENCRYPTION")
    encrypted = consumption_measure.measure(
        lambda: crypt_obj.encrypt(original_file, "shouvik"),
        epoch=2*20
    )
    with open('data/encrypted/encrypted.txt', 'wb') as e:
        e.write(encrypted)
    print("Energy Consumption (in micro Joules)", consumption_measure.get_energy_consumption())
    print("Time Taken (in microseconds)", consumption_measure.get_duration())

    encrypted = open("data/encrypted/encrypted.txt", "rb").read()
    print("\n\nDECRYPTION")
    decrypted = consumption_measure.measure(
        lambda: crypt_obj.decrypt(encrypted, "shouvik"),
        epoch=2*20
    )
    with open('data/decrypted/decrypted.txt', 'wb') as d:
        d.write(decrypted)

    print("Energy Consumption (in micro Joules)", consumption_measure.get_energy_consumption())
    print("Time Taken (in microseconds)", consumption_measure.get_duration())

    a = original_file
    b = open('data/decrypted/decrypted.txt', 'rb').read()
    from hashlib import sha1
    print(sha1(a).hexdigest() == sha1(b).hexdigest())
