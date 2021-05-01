alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
text = 'SHELL{P1Z_W3AR_4_M45K}'
key = 7
def encoder(text, key):
    encrypted_txt = ''
    for i in range(0,len(text)):
        if (text[i] == '{' or text[i] == '}' or text[i] == '_' or text[i].isdigit()):
            encrypted_txt += text[i]
        else:
            pos = alpha.find(text[i])
            pos = pos+key
            if pos >= len(alpha):
                encrypted_txt += alpha[pos - len(alpha)]
            else:
                encrypted_txt += alpha[pos]
    return encrypted_txt
ciphered_txt = encoder(text,key)
print(ciphered_txt)

def decoder(ciphered_txt,key):
    decrypted_txt = ''
    for i in range(0, len(ciphered_txt)):
        if (ciphered_txt[i] == '{' or ciphered_txt[i] == '}' or ciphered_txt[i] == '_' or ciphered_txt[i].isdigit()):
            decrypted_txt += ciphered_txt[i]
        else:
            pos = alpha.find(ciphered_txt[i])
            pos = pos - key
            if pos < 0:
                decrypted_txt += alpha[pos + len(alpha)]
            else:
                decrypted_txt += alpha[pos]
    return decrypted_txt
deciphered_txt = decoder(ciphered_txt,key)
print(deciphered_txt)
