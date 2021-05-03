from pwn import *
import base64
flag = "shell{"


for k in range(1,11):
	p=process("./encrypt.py")
	p.recvuntil("Crewmate! enter your situation report: ")
	my_msg='a'*16+'a'*(10-k)
	p.sendline(my_msg)
	enc_msg = p.recv(1024)
	p.close()
	enc_msg=base64.b64decode(enc_msg)
	enc_msg=enc_msg[32:47]

	for i in range(32,128):
		p1=process("./encrypt.py")
		p1.recvuntil("Crewmate! enter your situation report: ")
		my_msg='a'*(10-k)+flag+chr(i)
		p1.sendline(my_msg)
		enc_msg2 = p1.recv(1024)
		p1.close()
		enc_msg2=base64.b64decode(enc_msg2)
		enc_msg2=enc_msg2[16:31]

		if(enc_msg2==enc_msg):
			flag+=chr(i)
			break
print(flag)







