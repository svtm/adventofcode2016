
count = 0

for line in open("inputs/3"):
    sides = line.rstrip().split()
    side1 = int(sides[0])
    side2 = int(sides[1])
    side3 = int(sides[2])
    if (side1+side2) > side3 and (side1+side3) > side2 and (side2+side3) > side1:
        count += 1

print(count)

## part 2

count = 0
with open("inputs/3", 'r') as f:
    lines = f.readlines()
    for i in range(0, len(lines), 3):
        line1 = list(map(int, lines[i].rstrip().split()))
        line2 = list(map(int, lines[i+1].rstrip().split()))
        line3 = list(map(int, lines[i+2].rstrip().split()))
        for j in range(3):
            if line1[j] + line2[j] > line3[j] and line1[j] + line3[j] > line2[j] and line2[j] + line3[j] > line1[j]:
                count += 1

print(count)
