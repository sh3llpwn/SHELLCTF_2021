#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <openssl/sha.h>

void sha256sum(unsigned char input[],unsigned input_length,unsigned char output[])
{
	SHA256(input,input_length,output);
}


void displayHash(unsigned char hashString[])
{    
    int i;
    for (i = 0; i < 32; i++) {
        printf("%02x", hashString[i]);
    }
    printf("\n");
}

int main()
{
    uint64_t iterations = 0xFFFFFFF;
    unsigned char a_string[32] = "awesome_secure_password";
    unsigned char b_string[32];
    
    sha256sum(a_string,strlen((const char*)a_string),b_string);

    for(uint64_t i=0;i<(iterations/2);i++){
        sha256sum(b_string,32,a_string);
        sha256sum(a_string,32,b_string);
    }
    displayHash(b_string);

    return 0;
}
