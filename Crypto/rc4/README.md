# flag
SHELL{S4SKU3_UCH1H4}

# solution
given:
cipher_text :
a7 f9 de 54 29 92 7f 61 9a 7a 5f f3 f4 1a 88 a1 8f ca 97 47
(this is in hex)
key = 'MANGEKYOU'

and the hint is given that this is rc4 cipher i.e.
we need to perform 2 algos on key i.e 
key scheduling and psudo random generator.

after performing those two algorithms we get the key stream 
by xoring the key stream and ciphered text we get the original text.
this is the output of the python code which i used for encryption of the flag.
![rc4_flag](https://user-images.githubusercontent.com/70768880/119309775-615f2200-bc8c-11eb-898b-2a68c54a0f6f.png)

