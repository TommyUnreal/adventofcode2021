import os
from constraint import *

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def decode_digit(digit, key):
    retval = ""
    key = dict(zip(key.values(),key.keys()))
    for char in digit:
        retval += key[char]
    return retval

def get_decoded_output(digit, key):
    match len(digit):
        case 2:
            decoded = decode_digit(digit, key)
            return 1
        case 3:
            return 7
        case 4:
            return 4
        case 5:
            decoded = decode_digit(digit, key)
            if   ("b" not in decoded) and ("f" not in decoded):
                return 2
            elif ("b" not in decoded) and ("e" not in decoded):
                return 3
            else:
                return 5
        case 6:
            decoded = decode_digit(digit, key)
            if   ("c" not in decoded):
                return 6
            elif ("e" not in decoded):
                return 9
            else:
                return 0
        case 7:
            return 8

with open(os.path.join(__location__,"input.txt")) as file:

    sum = 0

    while True:
        input_line = file.readline().strip()
        if not input_line:
            break

        problem = Problem()

        input, four_digit_output = input_line.split("|")
        input = input.split()
        four_digit_output = four_digit_output.split()
        signals = list("abcdefg")
        segmets = list("abcdefg")

        for s in segmets:
            problem.addVariables(s,signals)

        problem.addConstraint(AllDifferentConstraint())

        for digit in input:
            match len(digit):
                case 2:
                    problem.addConstraint(InSetConstraint(list(digit)), list("cf"))
                case 3:
                    problem.addConstraint(InSetConstraint(list(digit)), list("acf"))
                case 4:
                    problem.addConstraint(InSetConstraint(list(digit)), list("bcdf"))
                case 5:
                    problem.addConstraint(InSetConstraint(list(digit)), list("ag"))
                case 6:
                    problem.addConstraint(InSetConstraint(list(digit)), list("abfg"))

        solution = problem.getSolutions()
        #key = solution['a'] + solution['b'] + solution['c'] + solution['d'] + solution['f'] + solution['g']
        #for s in problem.getSolutions():
        #    print(f"KEY ({key}): a = {s['a']}, b = {s['b']}, c = {s['c']}, d = {s['d']}, e = {s['e']}, f = {s['f']}, g = {s['g']}")

        output = 0
        for i in range(len(four_digit_output)):
            output += 10**(3-i) * get_decoded_output(four_digit_output[i], solution[0])

        sum += output
        print(output, solution[0])

print(f"sum: {sum}")