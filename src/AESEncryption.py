from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os


def AESEncryption():
    #defining relative file paths
    keyFilePath = os.path.join(os.path.dirname(__file__), '..', 'data', 'key.txt')
    plainTextFilePath = os.path.join(os.path.dirname(__file__), '..', 'data', 'plaintext.txt')
    cipherTextFilePath = os.path.join(os.path.dirname(__file__), '..', 'data', 'ciphertext.txt')
    ivFilePath = os.path.join(os.path.dirname(__file__), '..', 'data', 'iv.txt')
    
    #read hex key from file and convert to bytes
    key = bytes.fromhex(open(keyFilePath).read())
    #read plaintext from file and pad so that it's a multiple of 16
    m = pad(open(plainTextFilePath).read().encode(), 16)
    #generate iv - 16 bytes
    iv = get_random_bytes(16)
    
    #write iv in hex to iv file
    f = open(ivFilePath, 'w')
    f.write(iv.hex())
    f.close()
    
    #encrypt padded plaintext then output to terminal and file
    CBC = AES.new(key, AES.MODE_CBC, iv)
    c = CBC.encrypt(m)
    f = open(cipherTextFilePath, 'w')
    f.write(c.hex())
    print('Cipher text is ' + c.hex())
    
    