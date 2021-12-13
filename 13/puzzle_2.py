import os
import numpy as np
from numpy.lib.function_base import delete

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

output = []
dots   = []
folds  = []
max_x  = 0
max_y  = 0

with open(os.path.join(__location__,"input.txt")) as file:
    lines = list(line for line in (l.strip() for l in file) if line)
    for input_line in lines:       
        if "," in input_line:
            dots.append(list(map(int, input_line.split(","))))
            max_x = max(max_x, dots[-1][1])
            max_y = max(max_y, dots[-1][0])
        if "=" in input_line:
            input_line = input_line.split("=")
            if "x" in input_line[0]:
                folds.append(("x", int(input_line[1])))
            else:
                folds.append(("y", int(input_line[1])))

#fill dots onto transparent paper 
#+2 instead of +1 is hack for last empty column
output = np.zeros([max_x+2, max_y+1])
for dot in dots:
    output[dot[1], dot[0]] = 1

#folding paper
for axis, fold in folds:
    match axis:
        case "x":
            part_a, part_b = np.array_split(output, [fold], axis=1)
            part_b = np.delete(part_b, 0, axis=1)
            output = part_a + np.flip(part_b, axis=1)
        case "y":
            part_a, part_b = np.array_split(output, [fold], axis=0)
            part_b = np.delete(part_b, 0, axis=0)
            output = part_a + np.flip(part_b, axis=0)

#pretty print
for row in list(output):
    for column in row:
        if column:
            print("#", end="")
        else:
            print(" ", end="")
    print()