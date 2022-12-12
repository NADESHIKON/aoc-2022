with open("./input.txt") as file:
    for packet in file.read().split("\n"):
        lower = 0
        upper = lower + 4

        for i in range(len(packet) - 3):
            sub = packet[lower:upper]
            print(sub)
            if len(set(sub)) != len(sub):
                lower += 1
                upper += 1
            else:
                print(upper)
                break
