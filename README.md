# Crypto Algorithm Analyzer (CAA)
This project aims to develop a Python program to compare different Symmetric algorithms and Hashing functions based on given set of parameters:
1. File Size of .txt files (100Kb to 1Gb)
2. Mode (Encryption/Decryption)
3. Time Consumption (µs)
4. Energy Consumption (µJ)

##### ``The results of the comparison parameters of each algorithm are stored in CSV file format.``


## Algorithms Used
### Symmetric Algorithms:
1. AES-128
2. AES-256
3. Blowfish
4. Twofish

### Hashing Functions:
1. MD-2
2. MD-4
3. MD-5
5. RIPEMD-160
6. Whirlpool
7. SHA-1
8. SHA-224
9. SHA-256
10. SHA-384
11. SHA-512


## Technologies:
1. [hashlib](https://docs.python.org/3/library/hashlib.html)
2. [Numpy](https://numpy.org/doc/stable/)
3. [Pandas](https://pandas.pydata.org/docs/)
4. [Pycryptodome](https://pycryptodome.readthedocs.io/en/latest/)
5. [pyRAPL](https://pyrapl.readthedocs.io/en/stable/)
6. [Twofish](https://pypi.org/project/twofish/)
7. [Whirlpool](https://pypi.org/project/Whirlpool/)


## Setup
To run this project locally,
1. Install Python 3.5 or above in your system. To download the latest version of Python, [click here](https://www.python.org/downloads/)
2. Install the necessary required libraries and its dependencies locally in the system, open Command Prompt and run:  
``pip install -r requirements.txt``
3. Set appropiate values of the following variables in `main.py`:
  * ``ALGORITHM``
  * ``FILE_NAME``
  * ``MODE`` (Encryption/Decryption/Hashing)
  * ``PASSWORD``
  * ``EPOCH`` (Number of iteratons for average)
4. Open Command Prompt at root folder of this project and run:  
``python main.py``

