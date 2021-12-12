import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# def find_path(graph, start, end, path=[]):
#     path = path + [start]
#     if start == end:
#         return path
#     if start not in graph:
#         return None
#     for node in graph[start]:
#         if node not in path:
#             newpath = find_path(graph, node, end, path)
#             if newpath: return newpath
#     return None

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path or node != node.lower():
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

input_data  = []
output      = []

with open(os.path.join(__location__,"input.txt")) as file:
    while True:
        input_line = file.readline().strip()
        if not input_line:
            break

        input_data.append(input_line.split("-"))

list_of_vertices = set([j for i in input_data for j in i])
cave_system = dict()

for vertex in list_of_vertices:
    cave_system[vertex] = []

for path in input_data:
    if path[1] not in set(cave_system[path[0]]):
        cave_system[path[0]].append(path[1])
        cave_system[path[1]].append(path[0])

print(len(find_all_paths(cave_system,"start", "end")))