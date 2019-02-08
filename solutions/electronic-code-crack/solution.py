import requests
import string


def encrypt(message):
    return requests.post("http://10.0.10.10:5004/encrypt",
                         data={"message": message}).content.decode("hex")

def chunk(s):
    assert len(s) % 16 == 0
    num = len(s) / 16
    out = []
    for i in xrange(num):
        out.append(s[i * 16:(i + 1) * 16])
    return out

def find_padding_length():
    msg = chr(16) * 16
    for i in xrange(16):
        chunks = chunk(encrypt(msg + "a" * i))
        if chunks[1] == chunks[-1]:
            return i

def pad(s):
    extra = 16 - (len(s) % 16)
    return s + (chr(extra) * extra)

def leak_byte(starter):
    extra = find_padding_length() * "a"
    for char in string.ascii_letters + string.digits + "{}":
        chunks = chunk(encrypt(pad(char + starter) + extra + ("a" * (len(starter) + 1))))
        if chunks[1] == chunks[-1]:
            return char
    return None

flag = ""
for _ in xrange(15):
    flag = leak_byte(flag) + flag

print flag
