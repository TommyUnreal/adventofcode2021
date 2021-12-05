import os
import copy
from typing import Match

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

depth    = 0
position = 0

with open(os.path.join(__location__,"input.txt")) as file:
    line = [0]
    while line:
        line = file.readline().strip().split()
        if len(line) == 2 and line[1].isdigit():
            match line[0]:
                case "forward":
                    position += int(line[1])
                case "down":
                    depth    += int(line[1])
                case "up":
                    depth    -= int(line[1])  

print(depth*position, depth, position)