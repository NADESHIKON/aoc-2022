import re

crates = [
    list("ZJNWPS"),
    list("GST"),
    list("VQRLH"),
    list("VSTD"),
    list("QZTDBMJ"),
    list("MWTJDCZL"),
    list("LPMWGTJ"),
    list("NGMTBFQH"),
    list("RDGCPBQW")
]

with open("./input.txt") as file:
    regex = re.compile("move (\d{,2}) from (\d{,2}) to (\d{,2})")
    for move in file.read().split("\n"):
        print(move)
        move = list(map(lambda x: list(map(lambda y: int(y), list(x))), list(regex.findall(move))))[0]

        amount, from_index, to_index = move

        moved = []

        for i in range(amount):
            moved.append(crates[from_index - 1].pop())

        moved.reverse()
        for m in moved:
            crates[to_index - 1].append(m)

        print(crates)

    result = ""

    for crate in crates:
        result += "" if len(crate) == 0 else crate.pop()

    print(result)