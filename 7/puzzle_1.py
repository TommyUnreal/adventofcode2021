import os
from collections import Counter
from statistics import median

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

horizontal_positions = []
fuel_burned          = 0

with open(os.path.join(__location__,"input.txt")) as file:
    horizontal_positions = list(map(int, file.readline().strip().split(",")))

average_positions = round(median(horizontal_positions))

for pos in horizontal_positions:
    fuel_burned += abs(average_positions-pos)
    print(abs(average_positions-pos))

print(fuel_burned)