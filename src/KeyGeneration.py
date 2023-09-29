from Crypto.Random import get_random_bytes
import os

def KeyGeneration():
    keyFilePath = os.path.join(os.path.dirname(__file__), '..', 'data', 'key.txt')
    #generate random key with 32 bytes
    key = get_random_bytes(32)
    #print to terminal and write hex key to file
    print('Key has been generated: ' + key.hex())
    f = open(keyFilePath, 'w')
    f.write(key.hex())
    f.close()