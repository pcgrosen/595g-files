import requests
import json
import re


USERNAME = "test"
REMOTE = "http://10.0.10.10:5006"

# Log in to acquire the encrypted cookie
r = requests.post(REMOTE, data={"username": USERNAME})

# Create a mirror copy of the json that the server created
# We know how the server created it, so we can make ours in the same way
payload = {"username": USERNAME, "admin": 0}
dump = json.dumps(payload, sort_keys=True)

# Find the 0 in the json payload
offset = dump.index("0")

# Grab the IV from the cookies
iv = r.history[0].cookies["iv"].decode("hex")

# Create a bytearray (essentially a mutable string) copy of the iv
ivb = bytearray(iv)

# Flip the bottom bit of the corresponding byte, which will change the 0 to a 1
ivb[offset] ^= 1

r = requests.get(REMOTE + "/loggedin",
                 cookies={"iv": str(ivb).encode("hex"),
                          "payload": r.history[0].cookies["payload"]})

print re.search(r"595g\{[a-zA-Z0-9]+\}", r.content).group(0)
