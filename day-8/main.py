with open("./input.txt") as file:
    trees = []

    for t in file.read().split("\n"):
        trees.append(*list(map(lambda x: list(map(lambda y: int(y), list(x))), t.split())))

    count = 0

    for i in range(1, len(trees) - 1):
        for j in range(1, len(trees[0]) - 1):
            tree = trees[i][j]

            # left, right, top, bottom
            ranges = [[-j, 0, 0, 1], [1, len(trees[0]), 0, -1], [-i, 0, 1, 0], [1, len(trees), -1, 0]]

            v = False

            for r in ranges:
                viewable = True

                for k in range(1, max(len(trees), len(trees[0]))):
                    A = i + k * r[2]
                    B = j + k * r[3]
                    if 0 <= A < len(trees) and 0 <= B < len(trees[0]):
                        neighbor = trees[A][B]
                        # print(i + k, j + k, neighbor, tree)
                        if neighbor >= tree:
                            viewable = False

                if viewable:
                    v = True

            if v:
                count += 1

    count += len(trees) * 2 + len(trees[0]) * 2
    count -= 4

    print(count)