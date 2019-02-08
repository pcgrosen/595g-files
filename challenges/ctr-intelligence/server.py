import os
import random
import string
import struct
from Crypto.Cipher import AES
from flask import Flask, request, render_template, make_response, redirect

app = Flask(__name__)

admin = "admin"
KEY = "".join(random.choice(string.ascii_letters) for _ in xrange(16))
here = os.path.dirname(os.path.abspath(__file__))
flag_path = os.path.join(here, "flag")

def get_flag():
    with open(flag_path, "rb") as f:
        return f.read().strip()

def xor_strings(s1, s2):
    out = ""
    for c1, c2 in zip(s1, s2):
        out += chr(ord(c1) ^ ord(c2))
    return out

def crypt(instr, nonce):
    num_blocks = int(len(instr) / 16) + 1
    aes = AES.new(KEY, AES.MODE_ECB)
    # The following line creates a list of 16-byte blocks of the form
    #     <8 bytes of nonce><8 bytes of counter>
    plain_blocks = [struct.pack("<QQ", nonce, i) for i in xrange(num_blocks)]
    stream = "".join(map(aes.encrypt, plain_blocks))
    return xor_strings(instr, stream)

@app.route("/loggedin", methods=["GET"])
def loggedin_page():
    nonce = int(request.cookies["nonce"])
    enc = request.cookies["username"].decode("hex")
    dec = crypt(enc, nonce)
    if dec == admin:
        return render_template("admin.html", flag=get_flag())
    else:
        return render_template("loggedin.html",
                               msg="Thank you for signing in, %s." % (dec.encode("hex"),))

@app.route("/", methods=["GET", "POST"])
def login_page():
    if request.method == "GET":
        return render_template("login.html")
    else:
        if request.form["username"] == admin:
            return "You may not log in as admin.", 403
        else:
            resp = make_response(redirect("/loggedin"))
            nonce = random.randint(0, (1 << 64) - 1)
            resp.set_cookie("nonce", str(nonce))
            enc = crypt(request.form["username"], nonce)
            resp.set_cookie("username", enc.encode("hex"))
            return resp

if __name__ == "__main__":
    app.run("0.0.0.0", port=5005)
