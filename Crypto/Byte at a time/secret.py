import hashlib
iv  = hashlib.sha256("".encode()).digest()[:16]
key = hashlib.sha256("".encode()).digest()[:16]
flag = "shell{mySuper-secret-FlaGGG}"