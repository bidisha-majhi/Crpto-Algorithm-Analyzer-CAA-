import os
from algorithms.symmetric_algorithms import *
from algorithms.hash_functions import *
from utils.consumption import ConsumptionMeasure
from utils.csv_generator import CSVGenerator

ORIGINAL_FILE_BASE_PATH = "data/original/"
ENCRYPTED_FILE_BASE_PATH = "data/encrypted/"
DECRYPTED_FILE_BASE_PATH = "data/decrypted/"

ALGORITHM = CryptographerBlowfish()
FILE_NAME = "file_1GB.txt"
MODE = "DECRYPTION"
PASSWORD = "Shouvik"
FILE_INPUT_PATH = (ORIGINAL_FILE_BASE_PATH if MODE.lower() != "decryption" else ENCRYPTED_FILE_BASE_PATH) + FILE_NAME
FILE_SIZE = os.path.getsize(FILE_INPUT_PATH)

#CONSUMPTION MEASURE PARAMETERS
EPOCH = 2**3

#CSV GENERATOR PARAMETERS
PREVIOUS_OUTPUT = "Results_Symmetric_Algorithms.csv" if MODE.lower() != "hashing" else "Results_Hashing_Functions.csv"
OUTPUT = "Results_Symmetric_Algorithms.csv" if MODE.lower() != "hashing" else "Results_Hashing_Functions.csv"
INDEX = None

if __name__ == "__main__":
    crypt_obj = ALGORITHM

    pre, ext = os.path.splitext(FILE_NAME)

    print(f"Reading File {FILE_NAME} for {MODE.title()}...")
    with open(FILE_INPUT_PATH, "rb") as f:
        original_file = f.read()
    print(f"Successfully Read File {FILE_NAME} for {MODE.title()}\n")

    print(f"Performing {MODE.title()} with EPOCH {EPOCH} with Consumption Measure...")
    consumption_measure = ConsumptionMeasure()
    if MODE.lower() == "encryption":
        func = lambda: crypt_obj.encrypt(original_file, PASSWORD)
    elif MODE.lower() == "decryption":
        func = lambda: crypt_obj.decrypt(original_file, PASSWORD)
    else:
        func = lambda: crypt_obj.encrypt(original_file)
    file_output = consumption_measure.measure(
        func,
        epoch=EPOCH
    )
    print(f"{MODE.title()} Completed Successfully with Consumption Measure\n")

    if MODE.lower() != "hashing":
        print(f"Saving {MODE.title()} Output...")
        file_output_path = ENCRYPTED_FILE_BASE_PATH+FILE_NAME if MODE.lower() == "encryption" else DECRYPTED_FILE_BASE_PATH+FILE_NAME
        with open(file_output_path, 'wb') as f:
            f.write(file_output)
        print(f"Successfully saved {MODE.title()} Output to File: {file_output_path}\n")
    else:
        print(f"Hash Generated: {file_output}\n")

    print(f"\nSaving Consumption Measure Data...")
    result = CSVGenerator(output_csv=PREVIOUS_OUTPUT)

    algorithm = (type(ALGORITHM).__name__.replace("Cryptographer", "") + " " + str(ALGORITHM.__dict__.get('type', ""))).upper().strip()
    file_name = FILE_NAME
    file_size = FILE_SIZE
    mode = MODE.upper()
    duration = consumption_measure.get_duration()
    energy_consumed = consumption_measure.get_energy_consumption()

    result.add_or_update_value(
        algorithm=algorithm,
        file_name=file_name,
        file_size=file_size,
        mode=mode,
        duration=duration,
        energy_consumed=energy_consumed,
        index=INDEX
    )
    result.reset_index()
    result.save_csv(file_name=OUTPUT)

    print("")
    print("ALGORITHM:", algorithm)
    print("FILE NAME:", file_name)
    print("FILE SIZE (in bytes):", file_size)
    print("MODE:", mode)
    print("DURATION (in microseconds): ", duration)
    print("ENERGY CONSUMED (in micro Joules)", consumption_measure.get_energy_consumption())
    print("")

    print("Sucessfully Saved Consumption Measure Data.")

