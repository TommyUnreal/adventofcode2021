import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

n = 0

with open(os.path.join(__location__,"input.txt")) as file:
    line_last = int(file.readline().strip())
    line = 0 + line_last
    while line:
        line = file.readline().strip()
        if line.isdigit():
            line = int(line)
            if line > line_last:
                n += 1
            line_last = line

print(n)