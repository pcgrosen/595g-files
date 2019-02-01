import os
import random
import string
from Crypto.Cipher import AES
from flask import Flask, request, render_template

app = Flask(__name__)

KEY = "".join(random.choice(string.ascii_letters) for _ in xrange(16))
MESSAGE = "Remember this : {msg}. Oh, and this: {flag}"
here = os.path.dirname(os.path.abspath(__file__))
flag_path = os.path.join(here, "flag")

def pad(s):
    extra = 16 - (len(s) % 16)
    return s + (chr(extra) * extra)

def get_flag():
    with open(flag_path, "rb") as f:
        return f.read().strip()

@app.route("/", methods=["GET", "POST"])
def message_page():
    return render_template("home.html")

@app.route("/encrypt", methods=["POST"])
def encrypt_page():
    data = request.form["message"]
    aes = AES.new(KEY, AES.MODE_ECB)
    enc = aes.encrypt(pad(MESSAGE.format(msg=data, flag=get_flag())))
    return enc.encode("hex")

if __name__ == "__main__":
    app.run("0.0.0.0", port=5004)
