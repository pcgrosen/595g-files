import os
import json
import random
import string
from Crypto.Cipher import AES
from flask import Flask, request, render_template, make_response, redirect

app = Flask(__name__)

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

# Implements CBC-mode encryption
def encrypt(instr, iv):
    if len(instr) % 16 != 0:
        raise ValueError("Invalid instr length")
    num_blocks = len(instr) / 16
    aes = AES.new(KEY, AES.MODE_ECB)
    out = ""
    for i in xrange(num_blocks):
        if i == 0:
            prev = iv
        else:
            prev = out[(i - 1) * 16:i* 16]

        this_block = instr[i * 16:(i + 1) * 16]
        xored = xor_strings(this_block, prev)
        out += aes.encrypt(xored)
    return out

def decrypt(instr, iv):
    if len(instr) % 16 != 0:
        raise ValueError("Invalid instr length")
    num_blocks = len(instr) / 16
    aes = AES.new(KEY, AES.MODE_ECB)
    out = ""
    for i in xrange(num_blocks):
        if i == 0:
            prev = iv
        else:
            prev = instr[(i - 1) * 16:i* 16]

        this_block = instr[i * 16:(i + 1) * 16]
        ecb_dec = aes.decrypt(this_block)
        out += xor_strings(ecb_dec, prev)
    return out

@app.route("/loggedin", methods=["GET"])
def loggedin_page():
    iv = request.cookies["iv"].decode("hex")
    enc = request.cookies["payload"].decode("hex")

    try:
        dec_raw = decrypt(enc, iv)
    except ValueError:
        return "Error decrypting cookie", 400

    try:
        dec = json.loads(dec_raw)
    except ValueError:
        return "Error decoding cookie", 400

    if dec["admin"]:
        return render_template("admin.html", flag=get_flag())
    else:
        return render_template("loggedin.html",
                               msg="Thank you for signing in, %s." % (dec["username"].encode("hex"),))

@app.route("/", methods=["GET", "POST"])
def login_page():
    if request.method == "GET":
        return render_template("login.html")
    else:
        resp = make_response(redirect("/loggedin"))
        iv = os.urandom(16)
        resp.set_cookie("iv", iv.encode("hex"))
        payload = {"username": request.form["username"], "admin": 0}
        enc = encrypt(json.dumps(payload, sort_keys=True), iv)
        resp.set_cookie("payload", enc.encode("hex"))
        return resp

if __name__ == "__main__":
    app.run("0.0.0.0", port=5006)
