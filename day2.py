
keypad = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

row = 1
col  = 1

code = ""

for line in open('inputs/2'):
    for ch in line:
        if ch == "U" and row > 0:
            row -= 1
        elif ch == "D" and row < 2:
            row += 1
        elif ch == "L" and col > 0:
            col -= 1
        elif ch == "R" and col < 2:
            col += 1
    code += str(keypad[row][col])

print(code)


## part 2

keypad = [
            [False,     False,  1,      False,      False],
            [False,     2,      3,      4,          False],
            [5,         6,      7,      8,          9],
            [False,     "A",    "B",    "C",        False],
            [False,     False,  "D",    False,      False]
        ]

row = 2
col  = 0

code = ""

for line in open('inputs/2'):
    for ch in line:
        if ch == "U" and row > 0 and keypad[row-1][col]:
            row -= 1
        elif ch == "D" and row < 4 and keypad[row+1][col]:
            row += 1
        elif ch == "L" and col > 0 and keypad[row][col-1]:
            col -= 1
        elif ch == "R" and col < 4 and keypad[row][col+1]:
            col += 1
    code += str(keypad[row][col])

print(code)
