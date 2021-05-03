alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ{}_1234567890'
key   = 'QWERTPOIUYASDFGLKJHZXCVMNB{}_1234567890'

text = 'SHELL{5U65T1TUT10N_C1PH3R}'

def encrypter(text,key):
    encrypted_msg = ''
    for i in text:
        index = alpha.index(i)
        encrypted_msg += key[index]
    # print(encrypted_msg)
    return encrypted_msg

enc_msg = encrypter(text,key)
print(encrypter(text,key))

def decrypter(encyrptedMsg, key):
    decrypted_msg = ''
    for i in encyrptedMsg:
        index = key.index(i)
        decrypted_msg += alpha[index]
    return decrypted_msg

print(decrypter(enc_msg,key))







