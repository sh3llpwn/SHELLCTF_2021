# SecureShell Challenge
Recovering entropy states from logs to regenerate keys

## Building the challenge
0. (Optional) to randomize the keys again you can generate new keyfile using the keygen, which will overwrite the existing log file
```bash
rm -f private.pem  #remove existing key file
python3 keygen.py  #generate new key
```
this step does require pycryptodome to be installed.(easy to install with `pip3 install pycryptodome`)

1. Execute [build.sh](build.sh)
```
./build.sh
```
Done. 

## Deploying the challenge
1. DockerImage tag is "secureshell" so we can use it to deploy it as such :
```bash
docker run --name secureshell -d -p 4022:22 secureshell
```
where 4022 is the server port (-d to run it in background)

# Instructtions for CTF Players
```text
Ryan does not trust standard cryptography and thinks his implementations are better ...
can you prove him wrong !??

ServerIp : <ServerIp>
SSH Port : <ServerDockerSSHPort>
Username : shell
```
### Files to be provided
1. [keygen.log](keygen.log) logfile
2. [keygen.py](keygen.py) key generation script
3. [private.pem](private.pem) encrypted private key

## Hints:
1. (free) The private key is used to authenticate user `shell` for service ssh on server on the given port
2. (nearly free) Recover the data that you can

# Testing the challenge
1. Copy the Rand: Values from keygen.log file to crack.py 

Example:
```log
DEBUG : dKLen : 1 , Count : 1 , Rand : Cw== 
DEBUG : dKLen : 65 , Count : 2 , Rand : 7+lDRCiQiVqB5eGeON+buWPw0Kja8EqNISVawBuZTlciwK0oAm3s3mAwHV9Co8ON21yDsTOa+bHsMycQXPwTKsk= 
```
```python
# getting these values from key keygen.log
rand_rets = [
    b64decode("Cw==".encode()),
    b64decode("7+lDRCiQiVqB5eGeON+buWPw0Kja8EqNISVawBuZTlciwK0oAm3s3mAwHV9Co8ON21yDsTOa+bHsMycQXPwTKsk=".encode())
    ]
```

2. Run [solution/crack.py](solution/crack.py)
```log
Returning Cw== 
Returning 7+lDRCiQiVqB5eGeON+buWPw0Kja8EqNISVawBuZTlciwK0oAm3s3mAwHV9Co8ON21yDsTOa+bHsMycQXPwTKsk= 
-----BEGIN PRIVATE KEY-----
MIHuAgEAMBAGByqGSM49AgEGBSuBBAAjBIHWMIHTAgEBBEIB7+lDRCiQiVqB5eGe
ON+buWPw0Kja8EqNISVawBuZTlciwK0oAm3s3mAwHV9Co8ON21yDsTOa+bHsMycQ
XPwTKsqhgYkDgYYABAGRFtUwAaZsraczIXMO3LlNcT9MlFsqp/E1iI/qR8346atB
/aJwZVFMHPFD7VFIcGuOdSW4fCp2KQ2oQDkIlbCOogEKKkEhsbO9xyi35X3/dirg
WJZkflXUU5dcNFlgLIVZMm2h6CSoD8yjdHlLjGQtZ71I1iHE783KlivxpTeJYqkr
kg==
-----END PRIVATE KEY-----
```

3. try to ssh to the running container with this key 
```bash
chmod 400 decrypted_key
ssh -i decrypted_key shell@127.0.0.1 -p 4022
```

4. cat flag as user shell
```bash
cat flag.txt
```
