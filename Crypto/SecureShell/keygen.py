#!/usr/bin/python3
from Crypto.PublicKey import ECC
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from base64 import b64encode
import hashlib
import random
import logging
import string

secure_passphrase = open("secure_passphrase.txt",'r').read().strip()

LOGFILE = "keygen.log"
logging.basicConfig(filename=LOGFILE, filemode='w', format='%(levelname)s : %(message)s',level=logging.DEBUG)

entropy = entropy = ''.join(random.choices(string.ascii_letters + string.digits, k = 20 ))
salt = get_random_bytes(128)

logging.debug("Entropy : {}".format(entropy))
logging.debug("Salt : {}".format(b64encode(salt).decode()))

def s3cure_rand0m(i):
    s3cure_rand0m.count +=1
    rand = PBKDF2((entropy+hex(s3cure_rand0m.count)).encode(),salt,dkLen=i,count=1)
    logging.debug("dKLen : {} , Count : {} , Rand : {} ".format(i,s3cure_rand0m.count,b64encode(rand).decode()))
    return rand


logging.info("Generating an SSH private key")
s3cure_rand0m.count = 0
ecc = ECC.generate(curve='P-521',randfunc=s3cure_rand0m)
private_key = ecc.export_key(format='PEM',passphrase=secure_passphrase,protection="PBKDF2WithHMAC-SHA1AndAES128-CBC")
logging.info("Encrypted private key generated!")
logging.info("Writing key to file")
print(private_key)
open('private.pem','w').write(private_key)