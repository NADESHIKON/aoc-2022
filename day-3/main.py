pr = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("./input.txt") as file:
    priorities = 0

    for compartments in file.read().split("\n"):
        length = len(compartments)
        commons = set(compartments[0:length//2]) & set(compartments[length//2:])

        for i in commons:
            priorities += pr.index(i)


    print(priorities)
