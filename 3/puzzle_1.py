import os
import copy
from typing import Match

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

n_of_lines   = 0
active_bites = []

with open(os.path.join(__location__,"input.txt")) as file:
    line = "0"
    while line:
        line = file.readline().strip()
        #initialize
        if not active_bites:
            active_bites = [0] * len(line)
        for i in range(len(line)):
            if line[i] == "1":
                active_bites[i] += 1
        n_of_lines += 1

gamma_rate   = ""
epsilon_rate = ""

for bite in active_bites:
    if bite > n_of_lines / 2:
        gamma_rate   += "1"
        epsilon_rate += "0"
    else:
        gamma_rate   += "0"
        epsilon_rate += "1"

gamma_rate   = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)

print(gamma_rate*epsilon_rate)