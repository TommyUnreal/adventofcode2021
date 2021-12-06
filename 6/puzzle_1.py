import os
from collections import Counter

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

initial_state      = []
lanternfish_by_age = [0, 0, 0, 0, 0, 0, 0, 0, 0]
simulation_length  = 80

with open(os.path.join(__location__,"input.txt")) as file:
    initial_state = list(map(int, file.readline().strip().split(",")))

for state in initial_state:
    lanternfish_by_age[state] += 1

for day in range(simulation_length):
    new_fishes = lanternfish_by_age[0]
    for state in range(1,9):
        lanternfish_by_age[state-1] = lanternfish_by_age[state]
    lanternfish_by_age[8] = new_fishes
    lanternfish_by_age[6] += new_fishes

print(sum(lanternfish_by_age))