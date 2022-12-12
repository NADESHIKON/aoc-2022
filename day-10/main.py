def rotate(array, reverse):
    if reverse:
        array[:] = array[1:] + array[0:1]
    else:
        array[:] = array[-1:] + array[0:-1]
    return array

with open("./input.txt") as file:
    ops = file.read().split("\n")

    records = {20: 0, 60: 0, 100: 0, 140: 0, 180: 0, 220: 0}

    current = []
    display = []

    cycle = 0
    x = 1

    def increment():
        global cycle, x, current, display

        cycle += 1
        if cycle in records.keys():
            # print(cycle, x)
            records[cycle] = cycle * x

        if len(current) == 40:
            display.append(current)
            current = []

        current.append(sprite[(cycle - 1) % 40])

    sprite = list("###.....................................")

    for op in ops:
        if op == "noop":
            increment()
        elif op.startswith("addx"):
            v = int(op.split(" ")[1])
            increment()
            increment()
            x += v

            if v != 0:
                for i in range(0, abs(v)):
                    if v > 0:
                        sprite = rotate(sprite, False)
                    else:
                        sprite = rotate(sprite, True)

    print(sum(records.values()))

    display.append(current)
    for c in display:
        print("".join(c))
