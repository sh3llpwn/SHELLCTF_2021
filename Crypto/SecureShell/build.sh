#!/bin/bash
echo "[+] Make Sure to run python3 keygen.py before running build.sh"

read -rsp $'[+] Press any key to continue (or ctrl+c to quit)...\n' -n1 key

echo "[+] Building docker image for secureshell challenge"
secure_passphrase=$(cat secure_passphrase.txt)
chmod 400 private.pem

ssh-keygen -f private.pem -P $secure_passphrase -y > container/authorized_keys
if [ $? -eq 0 ];
then 
echo "[+] Written to authorized_keys succesfully";
echo "[+] Authorized_Keys : " && cat container/authorized_keys
else
echo "[-] Error";
exit
fi
docker build -t secureshell .