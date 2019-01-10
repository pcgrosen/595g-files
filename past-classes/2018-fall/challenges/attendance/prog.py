stuff = raw_input("do you want the flag? ")

if stuff.strip() == "yes":
    with open("flag", "rb") as f:
        flag = f.read()
    print "here you go:", flag
else:
    print "ok, bye"
