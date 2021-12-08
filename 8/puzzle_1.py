import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

digit_counter = 0

with open(os.path.join(__location__,"input.txt")) as file:
    while True:
        input_line = file.readline().strip()
        if not input_line:
            break
        four_digit_output = input_line.split("|")[1].split()

        for digit in four_digit_output:
            if len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7:
                digit_counter += 1

print(digit_counter)