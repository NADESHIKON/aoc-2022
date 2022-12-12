def twist_score(diff):
    return (diff > 0) - (diff < 0)


directions = {
    "U": (0, 1),
    "D": (0, -1),
    "R": (1, 0),
    "L": (-1, 0)
}

with open("./input.txt") as file:
    motions = list(map(lambda x: [x.split(" ")[0], int(x.split(" ")[1])], file.read().split("\n")))

    rope = [(0, 0) for _ in range(10)]

    visited = set()

    visited.add(rope[-1])

    for motion in motions:
        direction, steps = motion

        for step in range(steps):
            rope[0] = tuple(sum(x) for x in zip(rope[0], directions[direction]))

            for i in range(1, len(rope)):
                dx = rope[i - 1][0] - rope[i][0]
                dy = rope[i - 1][1] - rope[i][1]

                if abs(dx) > 1 or abs(dy) > 1:
                    rope[i] = tuple(sum(x) for x in zip(rope[i], [twist_score(dx), twist_score(dy)]))

            visited.add(rope[-1])

    print(len(visited))
