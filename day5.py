import hashlib

doorid = "ugkcyxxp"

password = [False for i in range(8)]

salt = 0
count = 0
while count < 8:
    hashed = ""
    while (hashed[:5] != "00000"):
        salt += 1
        m = hashlib.md5()
        string = (doorid + str(salt)).encode()
        m.update(string)
        hashed = m.hexdigest()
    try:
        index = int(hashed[5])
        if index < 8 and index >= 0 and not password[index]:
            ch = hashed[6]
            password[index] = ch
            print("Pos " + str(index) + " is " + ch)
            count += 1
    except Exception as ex:
        print("Index is invalid: " + hashed[5])

print("".join(password))
