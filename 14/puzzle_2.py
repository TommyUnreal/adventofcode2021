import os
from collections import Counter

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

input                = ""
polymer_template     = {}
pair_insertion_rules = {}
simulation_length    = 40
used_chars           = set()

with open(os.path.join(__location__,"input.txt")) as file:
    lines = list(line for line in (l.strip() for l in file) if line)
    for input_line in lines:       
        if "->" in input_line:
            key, val = input_line.split(" -> ")
            pair_insertion_rules[key] = [key[0] + val, val + key[1]]
            polymer_template[key]     = 0
            used_chars.add(key[0])
            used_chars.add(key[1])
        else:
            input = input_line

no_of_occurances = {char:0 for char in used_chars}

#add first and last element
no_of_occurances[input[0]] += 1
no_of_occurances[input[-1]] += 1

for j in range(1,len(input)):
    key = "".join(input[j-1:j+1])
    polymer_template[key] += 1

# compute all insertion
for i in range(simulation_length):
    temp = {key:0 for key in polymer_template.keys()}
    for pair in pair_insertion_rules.items():
        in0, in1 = pair[1]
        temp[in0] += polymer_template[pair[0]]
        temp[in1] += polymer_template[pair[0]]
    polymer_template = temp

#compute occurances
for pair in polymer_template.items():
    no_of_occurances[pair[0][0]] += pair[1]
    no_of_occurances[pair[0][1]] += pair[1]

#divide occurances by 2 (each component is presented twice in sum)
no_of_occurances = {key:int(val/2) for key,val in no_of_occurances.items()}

print(no_of_occurances[max(no_of_occurances, key=no_of_occurances.get)]-no_of_occurances[min(no_of_occurances, key=no_of_occurances.get)])