from base64 import b64decode,b64encode
from Crypto.Protocol.KDF import PBKDF2
from Crypto.PublicKey import ECC

# getting these values from key keygen.log
rand_rets = [
    b64decode("Cw==".encode()),
    b64decode("7+lDRCiQiVqB5eGeON+buWPw0Kja8EqNISVawBuZTlciwK0oAm3s3mAwHV9Co8ON21yDsTOa+bHsMycQXPwTKsk=".encode())
    ]

def s3cure_rand0m(i):
    var = rand_rets.pop(0)
    print("Returning {} ".format(b64encode(var).decode()))
    return var

key = ECC.generate(curve='P-521',randfunc=s3cure_rand0m)
private_key = key.export_key(format='PEM')
print(private_key)
open("decrypted_key",'w').write(private_key)