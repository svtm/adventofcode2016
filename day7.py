import re


def is_abba(string):
    for i in range(len(string)-3):
        if string[i] != string[i+1] and string[i+1] == string[i+2] and string[i] == string[i+3]:
            return True
    return False

def find_aba(string):
    res = []
    for i in range(len(string)-2):
        if string[i] != string[i+1] and string[i] == string[i+2]:
            res.append(string[i:i+3])
    return res

def check_aba_bab(abalist, bablist):
    for aba in abalist:
        for bab in bablist:
            if aba[0] == bab[1] and aba[1] == bab[0]:
                return True
    return False

count = 0
for line in open("inputs/7"):
    hypernet = re.findall(r"\[(.*?)\]", line)
    strings = [s.split(']')[-1] for s in line.split('[')]
    hyperABBA = False
    stringABBA = False
    for hyper in hypernet:
        if is_abba(hyper):
            hyperABBA = True
            break
    if hyperABBA:
        continue
    for string in strings:
        if stringABBA:
            break
        if is_abba(string):
            stringABBA = True
            count += 1
print(count)


## part 2:
count = 0
for line in open("inputs/7"):
    hypernet = re.findall(r"\[(.*?)\]", line)
    strings = [s.split(']')[-1] for s in line.split('[')]
    abalist = []
    bablist = []
    for hyper in hypernet:
        bab = find_aba(hyper)
        if bab:
            bablist.extend(bab)
    for string in strings:
        aba = find_aba(string)
        if aba:
            abalist.extend(aba)
    if abalist and bablist and check_aba_bab(abalist, bablist):
        count += 1
print(count)
