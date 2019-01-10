import random
import string


def encrypt(thing, key):
    out = ""
    for i in xrange(len(thing)):
        out += chr(ord(thing[i]) ^ ord(key[i % len(key)]))
    return out

KEY = "omegalul"
PASSWORD = encrypt("".join(random.choice(string.ascii_lowercase) for _ in xrange(20)), KEY)

print "Challenge:", PASSWORD.encode("hex")
stuff = raw_input("what's the password? ")

encrypted_stuff = encrypt(stuff.strip(), KEY)

if encrypted_stuff == PASSWORD:
    with open("flag", "rb") as f:
        flag = f.read()
    print "here you go:", flag
else:
    print "WRONG!"
