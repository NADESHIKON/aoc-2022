with open("input.txt", "r") as file:
    calories = []
    current = []

    lines = file.readlines()
    for i in range(len(lines)):
        a = lines[i]
        if a == "\n":
            calories.append(sum(current))
            current = []
        else:
            current.append(int(a))

    calories = sorted(calories, reverse=True)
    print(calories[0] + calories[1] + calories[2])