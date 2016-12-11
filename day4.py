
def get_dict():
    res = {}
    for i in range(97, 123):
        res[chr(i)] = 0
    return res

idSum = 0
validRooms = []

for line in open("inputs/4"):
    line = line.rstrip().split("-")
    strings = line[:-1]
    name = "".join(strings)
    roomID = line[-1].split("[")[0]
    checksum = line[-1].split("[")[1][:-1]

    alphabet = get_dict()
    for ch in name:
        alphabet[ch] += 1

    sortedChars = "".join([v[0] for v in sorted(alphabet.items(), key=lambda kv: (-kv[1], kv[0]))][:5])
    if sortedChars == checksum:
        strings.append(roomID)
        validRooms.append(strings)
        idSum += int(roomID)

print(idSum)

#valid ranges: 97-122
alphabet = [chr(i) for i in range(97, 123)]
for room in validRooms:
    roomid = int(room[-1])
    name = room[:-1]
    decrypted = ""
    for word in name:
        for ch in word:
            decrypted += alphabet[ (alphabet.index(ch) + roomid) % len(alphabet)]
        decrypted += " "
    if "northpole" in decrypted:
        print(decrypted + "- " + str(roomid))
