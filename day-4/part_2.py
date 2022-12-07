with open("./input.txt") as file:
    pairs = file.read().split("\n")

    overlaps = 0

    for pair in pairs:
        a, b = list(map(lambda x: list(map(lambda y: int(y), x.split("-"))), pair.split(",")))

        if max(a[0], b[0]) <= min(a[1], b[1]):
            overlaps += 1

    print(overlaps)
