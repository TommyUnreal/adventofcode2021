import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

cave_map = []
danger   = 0

with open(os.path.join(__location__,"input.txt")) as file:
    while True:
        input_line = file.readline().strip()
        if not input_line:
            break

        cave_map.append(list(map(int, list(input_line))))

    for i in range(len(cave_map)):
        for j in range(len(cave_map[i])):
            poi = []
            # top_left  = cave_map[i - 1][j - 1]
            # top       = cave_map[i    ][j - 1]
            # top_right = cave_map[i + 1][j - 1]

            # mid_left  = cave_map[i - 1][j    ]
            # mid_right = cave_map[i + 1][j    ]

            # bot_left  = cave_map[i - 1][j + 1]
            # bot       = cave_map[i    ][j + 1]
            # bot_right = cave_map[i + 1][j + 1]
            if i > 0:
                poi.append(cave_map[i - 1][j    ])
            if i < len(cave_map)-1:
                poi.append(cave_map[i + 1][j    ])            
            if j > 0:
                poi.append(cave_map[i    ][j - 1])
            if j < len(cave_map[i])-1:
                poi.append(cave_map[i    ][j + 1])
            if all(p > cave_map[i][j] for p in poi):
                danger += 1 + cave_map[i][j]

print(danger)