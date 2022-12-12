def bfs(start, hill_content):
    visited = set()
    queue = [(start, 0)]
    visited.add(start)

    while queue:
        node, length = queue.pop(0)
        i, j = node

        current = hill_content[i][j]

        if node == end:
            return length

        neighbor_indices = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

        for neighbor_index in neighbor_indices:
            x, y = neighbor_index

            if x < 0 or x >= len(hill) or y < 0 or y >= len(hill[x]):
                continue

            neighbor = hill_content[x][y]

            if neighbor_index not in visited:
                if neighbor - current <= 1:
                    queue.append((neighbor_index, length + 1))
                    visited.add(neighbor_index)

    return 888888888

with open("./input.txt") as file:
    hill = []
    starts = []

    end = (0, 0)

    lines = file.read().split("\n")
    for i in range(len(lines)):
        h = []

        line = lines[i]
        for j in range(len(line)):
            v = line[j]
            if v == "a":
                h.append(97)
                starts.append((i, j))
            else:
                if v == "E":
                    end = i, j
                    h.append(122)
                else:
                    h.append(ord(v))

        hill.append(h)

    steps = 99999999999999

    for start in starts:
        steps = min(steps, bfs(start, hill))

    print(steps)