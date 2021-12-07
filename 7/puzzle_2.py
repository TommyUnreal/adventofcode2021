import os
from collections import Counter
from statistics import median

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

horizontal_positions = []
fuel_burned          = 0

def get_fuel_burned(level):
    pos_sum = 0
    for pos in horizontal_positions:
        pos_sum += sum(list(range(1, abs(level-pos)+1)))
    return pos_sum

with open(os.path.join(__location__,"input.txt")) as file:
    horizontal_positions = list(map(int, file.readline().strip().split(",")))

#this is bruteforce solution and it sucks
# for i in range(max(horizontal_positions)):
#     pos_sum = 0
#     for pos in horizontal_positions:
#         pos_sum += sum(list(range(1, abs(i-pos)+1)))
#     fuel_burned.append(pos_sum)

average_positions    = round(median(horizontal_positions))
search_min_direction = 0

if get_fuel_burned(average_positions) > get_fuel_burned(average_positions+1): 
    search_min_direction = 1
elif get_fuel_burned(average_positions) < get_fuel_burned(average_positions+1):
    search_min_direction = -1

fuel_burned = get_fuel_burned(average_positions)
while True:
    average_positions += search_min_direction
    next_fuel_burned = get_fuel_burned(average_positions)
    if fuel_burned > next_fuel_burned:
        fuel_burned = next_fuel_burned
    else:
        break

print(fuel_burned)