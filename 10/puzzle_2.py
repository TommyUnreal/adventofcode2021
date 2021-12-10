import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

score       = []

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
                            stack = []
                            break
                    case "]":
                        if stack[-1] == "[":
                            stack.pop()
                        else:
                            stack = []
                            break
                    case "}":
                        if stack[-1] == "{":
                            stack.pop()
                        else:
                            stack = []
                            break
                    case ">":
                        if stack[-1] == "<":
                            stack.pop()
                        else:
                            stack = []
                            break
        
        subscore = 0

        if stack:
            for log in reversed(stack):
                match log:
                    case "(":
                        subscore = (subscore * 5) + 1
                    case "[":
                        subscore = (subscore * 5) + 2
                    case "{":
                        subscore = (subscore * 5) + 3
                    case "<":
                        subscore = (subscore * 5) + 4
        
            score.append(subscore)

print(sorted(score)[int(len(score) / 2)], score)