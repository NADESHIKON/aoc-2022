with open("./input.txt") as file:
    pairs = file.read().split("\n")

    overlaps = 0

    for pair in pairs:
        a, b = list(map(lambda x: list(map(lambda y: int(y), x.split("-"))), pair.split(",")))

        overlap = False

        if a[0] <= b[0] and a[1] >= b[1]:
            overlap = True
        elif a[0] >= b[0] and a[1] <= b[1]:
            overlap = True

        if overlap:
            overlaps += 1

    print(overlaps)
