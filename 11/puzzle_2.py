import os
import numpy as np

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

output     = 0
octopies   = []
sim_length = 0
flash_val  = 10

def add_one(indexes):
    global octopies
    if 0 <= indexes[0] <= 9 and 0 <= indexes[1] <= 9:
        octopies[indexes[0], indexes[1]] += 1

with open(os.path.join(__location__,"input.txt")) as file:
    while True:
        input_line = file.readline().strip()
        if not input_line:
            break

        octopies.append(list(map(int, list(input_line))))

octopies = np.array(octopies)
while True:
    print(f"After step {sim_length+1}:")
    octopies = octopies + 1
    while np.sum((octopies >= flash_val).astype(int)):
        flashes = (octopies >= flash_val).astype(int) #identify pixels with flashes
        output += np.sum(flashes)                     #add no. flashes to output
        for x, y in np.ndindex(flashes.shape):
            if flashes[x, y]:
                #octopies = add_one(octopies, [x  , y  ])
                add_one([x-1, y  ])
                add_one([x+1, y  ])
                add_one([x  , y+1])
                add_one([x  , y-1])
                add_one([x+1, y+1])
                add_one([x+1, y-1])
                add_one([x-1, y+1])
                add_one([x-1, y-1])
                octopies[x, y] = -flash_val

    octopies[octopies < 0] = 0
    sim_length            += 1
    if np.sum((octopies != 0).astype(int)) == 0:
        break

print(output)