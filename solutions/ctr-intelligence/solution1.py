import requests
import re


REMOTE = "http://10.0.10.10:5005"
USERNAME = "aaaaa"

def xor_strings(s1, s2):
    out = ""
    for c1, c2 in zip(s1, s2):
        out += chr(ord(c1) ^ ord(c2))
    return out

r = requests.post(REMOTE, data={"username": USERNAME})

stream = xor_strings(r.history[0].cookies["username"].decode("hex"), USERNAME)
admin_cookie = xor_strings(stream, "admin")

resp = requests.get(REMOTE + "/loggedin", cookies={"nonce": r.history[0].cookies["nonce"],
                                                   "username": admin_cookie.encode("hex")})
print re.search(r"595g\{[a-zA-Z0-9]+\}", resp.content).group(0)
