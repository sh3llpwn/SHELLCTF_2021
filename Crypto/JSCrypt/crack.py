import hashlib

iterations = 0xFFFFFFF
init_password = "awesome_secure_password"

passwd = init_password.encode()
for i in range(iterations):
    passwd = hashlib.sha256(passwd).digest()

print(passwd.hex())
