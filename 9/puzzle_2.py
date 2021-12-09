import os
from collections import Counter as cntr
import numpy as np
from scipy import ndimage

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

cave_map = []
output   = 1

with open(os.path.join(__location__,"input.txt")) as file:
    while True:
        input_line = file.readline().strip()
        if not input_line:
            break

        cave_map.append(list(map(int, list(input_line))))

np_cave_map = np.array(cave_map)
basins = np_cave_map < 9
labels, nlabels = ndimage.label(basins)
basin_sizes = cntr(sum(labels.tolist(),[]))
for key, value in basin_sizes.most_common(4):
    if key != 0:
        output *= value
print(output)