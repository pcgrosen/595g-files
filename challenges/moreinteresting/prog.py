
KEY = "omegalul"
PASSWORD = "\x06M\x17_A\x1f\x10\x0f\x1a\x1f\x00G\x11\r\x06\x1f\x18\x02\x17\x03A\x03\x00\x18O\x02\x03GY"

def encrypt(thing, key):
    return "".join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(thing))

stuff = raw_input("what's the password? ")

encrypted_stuff = encrypt(stuff.strip(), KEY)

if encrypted_stuff == PASSWORD:
    with open("flag", "rb") as f:
        flag = f.read()
    print "here you go:", flag
else:
    print "WRONG!"
