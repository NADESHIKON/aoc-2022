pr = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("./input.txt") as file:
    priorities = 0
    groups = list(zip(*(iter(file.read().split("\n")),) * 3))

    for group in groups:
        commons = set(group[0]) & set(group[1]) & set(group[2])

        for common in commons:
            priorities += pr.index(common)

    print(priorities)