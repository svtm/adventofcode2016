
results = [dict.fromkeys([chr(i) for i in range(97, 123)], 0) for i in range(8) ]

for line in open("inputs/6"):
    for i in range(len(line)-1):
        results[i][line[i]] += 1

message1 = ""
message2 = ""
for i in range(len(results)):
    message1 += max(results[i].keys(), key=(lambda key: results[i][key]))
    message2 += max(results[i].keys(), key=(lambda key: -results[i][key]))

print(message1)
print(message2)
