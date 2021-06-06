import string
import requests

SERVER_BASE_URL = "http://34.92.214.217:8000" 

possibleCharset = string.digits + string.ascii_letters+ "}{-_!@#$%^&*()+=<>.,;':[]|`~"

s = requests.Session()

def getCookie(username):
    data = {"username":username}
    ret = s.post(SERVER_BASE_URL + "/genCookie",json=data)
    return ret.json()["cookie"]

def findFlagLen():
    zeroLengthCookieLen = len(getCookie(""))
    for i in range(17):
        thisRequestLen = len(getCookie(" "*i))
        if zeroLengthCookieLen != thisRequestLen:
            flagLen = thisRequestLen//2 - i - 16
            return flagLen

def getEncFlagChars(chars,maxBlocks=3):
    void = (maxBlocks*16) - chars
    payload = " "*void
    cookie = getCookie(payload)
    return cookie[:maxBlocks*32]

def getCutomEncKnownChars(chars,maxBlocks=3):
    void = (maxBlocks*16) - len(chars)
    payload = " "*void + chars
    cookie = getCookie(payload)
    return cookie[:maxBlocks*32]

flagLen = findFlagLen()

global flag,maxBlocks
flag = ""
maxBlocks = (flagLen // 16) +1


print("[+] Found flag length = {} characters, using maxBlocks for ByteAtATime as {}".format(flagLen,maxBlocks))
print("[+] Finding Flag Now : ")
for index in range(flagLen):
    testAgainst = getEncFlagChars(index+1,maxBlocks)
    ctr = 0x00
    for char in possibleCharset:
        testData = flag + char
        testEnc = getCutomEncKnownChars(testData,maxBlocks)
        if testEnc == testAgainst:
            flag += char
            print("[+] Found next character : {} | [+] Flag : {} ".format(char,flag))
            break
        else:
            ctr +=1
    if ctr == len(possibleCharset):
        break

assert len(flag) == flagLen , "Error"
print("[+] Flag : {}".format(flag))
