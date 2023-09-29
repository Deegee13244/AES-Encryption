from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os

def AESDecryption():
    #defining relative file paths
    keyFilePath = os.path.join(os.path.dirname(__file__), '..', 'data', 'key.txt')
    resultFilePath = os.path.join(os.path.dirname(__file__), '..', 'data', 'result.txt')
    cipherTextFilePath = os.path.join(os.path.dirname(__file__), '..', 'data', 'ciphertext.txt')
    ivFilePath = os.path.join(os.path.dirname(__file__), '..', 'data', 'iv.txt')
    
    #read key, iv, and ciphertext from file and convert to bytes
    key = bytes.fromhex(open(keyFilePath).read())
    iv = bytes.fromhex(open(ivFilePath).read())
    c = bytes.fromhex(open(cipherTextFilePath).read())
    
    #decrypt and unpack new plaintext, write to terminal and file
    CBC = AES.new(key, AES.MODE_CBC, iv)
    m = unpad(CBC.decrypt(c), 16)
    f = open(resultFilePath, 'w')
    f.write(m.decode())
    f.close()
    print('Plaintext is: ' + m.decode())
    
    