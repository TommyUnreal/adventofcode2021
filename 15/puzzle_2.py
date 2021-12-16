import os
import networkx as nx
import numpy as np
#ýimport matplotlib.pyplot as plt

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

cave_map   = []

def add_edge(from_index, to_index):
    global cave_graph
    global cave_map
    if 0 <= to_index[0] < len(cave_map[0]) and 0 <= to_index[1] < len(cave_map):
        fi_name = str(from_index[0]) + "," + str(from_index[1])
        ti_name = str(to_index[0])   + "," + str(to_index[1])
        cave_graph.add_edge(fi_name, ti_name, weight=cave_map[to_index[0]][to_index[1]])

with open(os.path.join(__location__,"input.txt")) as file:
    lines = list(line for line in (l.strip() for l in file) if line)
    for input_line in lines:       
        cave_map.append(list(map(int, list(input_line))))

cave_map   = np.array(cave_map)
cave_map   = np.block([[(cave_map + y + x - 1) % 9 + 1 for x in range(5)] for y in range(5)])
cave_graph = nx.grid_2d_graph(len(cave_map[0]), len(cave_map), create_using=nx.DiGraph)

for y in range(len(cave_map)):
    for x in range(len(cave_map[y])):
            add_edge([x, y], [x-1, y  ])
            add_edge([x, y], [x+1, y  ])
            add_edge([x, y], [x  , y+1])
            add_edge([x, y], [x  , y-1])
            # add_edge([x, y], [x+1, y+1])
            # add_edge([x, y], [x+1, y-1])
            # add_edge([x, y], [x-1, y+1])
            # add_edge([x, y], [x-1, y-1])

print(nx.shortest_path_length(cave_graph, "0,0", str(len(cave_map[0])-1) + "," + str(len(cave_map)-1), weight="weight"))
# nx.draw(cave_graph)
# plt.show()