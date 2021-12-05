import os
import copy

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

n = 0

with open(os.path.join(__location__,"input.txt")) as file:
    line_last = [int(file.readline().strip()), int(file.readline().strip()), int(file.readline().strip())]
    line = []
    num = 1
    while num:
        num = file.readline().strip()
        if num.isdigit():
            line = copy.deepcopy(line_last)
            line.pop(0)
            line.append(int(num))
            if sum(line) > sum(line_last):
                n += 1
            line_last = copy.deepcopy(line)

print(n)