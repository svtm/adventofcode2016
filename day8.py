import os

WIDTH = 50
HEIGHT = 6

screen = [['.' for i in range(WIDTH)] for i in range(HEIGHT)]

def print_screen():
    for row in screen:
        r = ""
        for col in row:
            r += col
        print(r)
def rect(a, b):
    for row in range(b):
        for col in range(a):
            screen[row][col] = '#'

def rot_row(a, b):
    new_row = ['.' for i in range(WIDTH)]
    for i in range(WIDTH):
        new_row[i] = screen[a][(i-b) % WIDTH]
    screen[a] = new_row

def rot_col(a, b):
    new_col = ['.' for i in range(HEIGHT)]
    for i in range(HEIGHT):
        new_col[i] = screen[(i-b) % HEIGHT][a]
    for i in range(HEIGHT):
        screen[i][a] = new_col[i]

for line in open('inputs/8'):
    os.system('clear')
    line = line.rstrip().split()
    if line[0] == "rect":
        dims = list(map(int, line[1].split('x')))
        rect(dims[0], dims[1])
    elif line[0] == "rotate":
        b = int(line[-1])
        a = int(line[2].split("=")[1])
        if line[1] == "row":
            rot_row(a, b)
        else:
            rot_col(a, b)
    print_screen()

count = 0
for row in screen:
    for pixel in row:
        if pixel == '#':
            count += 1
print(count)
