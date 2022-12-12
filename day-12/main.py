with open("./input.txt") as file:
    hill = []
    start = (0, 0)
    end = (0, 0)

    lines = file.read().split("\n")
    for i in range(len(lines)):
        h = []

        line = lines[i]
        for j in range(len(line)):
            v = line[j]
            if v == "S":
                h.append(97)
                start = i, j
            else:
                if v == "E":
                    end = i, j
                    h.append(122)
                else:
                    h.append(ord(v))

        hill.append(h)

    for h in hill:
        print("".join(str(h)))

    visited = set()
    queue = [(start, 0)]
    visited.add(start)

    while queue:
        node, length = queue.pop(0)
        i, j = node

        current = hill[i][j]

        if node == end:
            print(length)
            break

        neighbor_indices = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

        for neighbor_index in neighbor_indices:
            x, y = neighbor_index

            if x < 0 or x >= len(hill) or y < 0 or y >= len(hill[x]):
                continue

            neighbor = hill[x][y]

            if neighbor_index not in visited:
                if neighbor - current <= 1:
                    queue.append((neighbor_index, length + 1))
                    visited.add(neighbor_index)