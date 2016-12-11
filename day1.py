direction = ["N", "E", "S", "W"]

currDir = 0

blocks = {"N": 0, "E": 0, "S": 0, "W": 0}


for line in open('inputs/1'):
    line = line.rstrip().split(", ")
    print(line)
    for command in line:
        print(command)
        print("Prev dir: " + direction[currDir])
        if command[0] == "L":
            currDir = (currDir - 1) % 4
        else:
            currDir = (currDir + 1) % 4
        print("New dir: " + direction[currDir])
        dist = int(command[1:])
        blocks[direction[currDir]] += dist

print(blocks)
totalDist = abs(blocks["N"] - blocks["S"]) + abs(blocks["E"] - blocks["W"])
print(totalDist)


## Part 2
grid = [[False for i in range(1000)] for i in range(1000)]
blocks = {"N": 0, "E": 0, "S": 0, "W": 0}
currDir = 0
x = 500
y = 500

found = False

for line in open('inputs/1'):
    line = line.rstrip().split(", ")
    for command in line:
        if found:
            break

        if command[0] == "L":
            currDir = (currDir - 1) % 4
        else:
            currDir = (currDir + 1) % 4
        dist = int(command[1:])
        print("Curr pos: " + str(x) + ", " + str(y))
        print("Going " + str(dist) + " in dir " + direction[currDir])
        for i in range(dist):
            if direction[currDir] == "N":
                x += 1
            elif direction[currDir] == "E":
                y += 1
            elif direction[currDir] == "S":
                x -= 1
            elif direction[currDir] == "W":
                y -= 1
            blocks[direction[currDir]] += 1
            if (grid[x][y]):
                totalDist = abs(blocks["N"] - blocks["S"]) + abs(blocks["E"] - blocks["W"])
                print("Prev visited! Dist: " + str(totalDist))
                found = True
            else:
                grid[x][y] = True
