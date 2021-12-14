import os
from collections import Counter

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

polymer_template     = ""
pair_insertion_rules = []
simulation_length    = 10

with open(os.path.join(__location__,"input.txt")) as file:
    lines = list(line for line in (l.strip() for l in file) if line)
    for input_line in lines:       
        if "->" in input_line:
            pair_insertion_rules.append(tuple(input_line.split(" -> ")))
        else:
            polymer_template = input_line

for i in range(simulation_length):
    temp_polymer = polymer_template[0]
    for j in range(1,len(polymer_template)):
        inserted = False
        for rule, insert in pair_insertion_rules:
            if polymer_template[j-1:j+1] == rule:
                temp_polymer = temp_polymer + insert + rule[1]
                inserted = True
                break
        if not inserted:
            temp_polymer += polymer_template[j]
    polymer_template = temp_polymer
    print(f"After step {i+1}: {polymer_template}")

polymer_template = Counter(polymer_template).most_common
print(polymer_template()[0][1]-polymer_template()[-1][1])