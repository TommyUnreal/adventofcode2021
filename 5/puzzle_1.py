import os
from collections import Counter

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

hydrothermal_vents = []

with open(os.path.join(__location__,"tinput.txt")) as file:
    while True:
        nextline = file.readline().strip()
        if not nextline:
            break
        
        pointA = list(map(int,nextline.split(" -> ")[0].split(",")))
        pointB = list(map(int,nextline.split(" -> ")[1].split(",")))
        
        if pointA[0] == pointB[0] or pointA[1] == pointB[1]:
            for i in range(min(pointA[0], pointB[0]), max(pointA[0], pointB[0])+1):
                for j in range(min(pointA[1], pointB[1]), max(pointA[1], pointB[1])+1):
                    hydrothermal_vents.append((i, j))
                    
filetered_hydrothermal_vents = {key : val for key, val in Counter(hydrothermal_vents).items() if (isinstance(val, int) and (val > 1))}

print(len(filetered_hydrothermal_vents))