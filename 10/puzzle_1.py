import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

score       = 0

with open(os.path.join(__location__,"input.txt")) as file:
    while True:
        input_line = file.readline().strip()
        if not input_line:
            break

        stack = []
        for char in list(input_line):
            if char in "([{<":
                stack.append(char)
            else:
                match char:
                    case ")":
                        if stack[-1] == "(":
                            stack.pop()
                        else:
                            score += 3
                            break
                    case "]":
                        if stack[-1] == "[":
                            stack.pop()
                        else:
                            score += 57
                            break
                    case "}":
                        if stack[-1] == "{":
                            stack.pop()
                        else:
                            score += 1197
                            break
                    case ">":
                        if stack[-1] == "<":
                            stack.pop()
                        else:
                            score += 25137
                            break
print(score)