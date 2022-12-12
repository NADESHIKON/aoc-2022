import sys


class Monkey:
    def __init__(self, items, operation, test, true_target, false_target):
        self.items = items
        self.operation = operation
        self.test = test
        self.true_target = true_target
        self.false_target = false_target
        self.inspect_times = 0

    def testVal(self, val):
        if self.test.strip().startswith("divisible by"):
            return val % int(self.test.split("divisible by ")[1]) == 0

        return False

    def operate(self, old):
        return int(eval(self.operation.strip().replace("old", str(old)).split("=")[1].strip()))

    def __str__(self):
        return f"{self.items} | {self.inspect_times}"

with open("./input.txt") as file:
    lines = file.read().split("\n")

    monkeys = []

    for i in range(0, len(lines), 7):
        sets = lines[i]
        if sets.startswith("Monkey"):
            start = list(map(lambda x: int(x), lines[i + 1].split(":")[1].split(",")))
            op = lines[i + 2].split(":")[1]
            test = lines[i + 3].split(":")[1]
            true = int(lines[i + 4].split("If true: throw to monkey ")[1])
            false = int(lines[i + 5].split("If false: throw to monkey ")[1])

            monkey = Monkey(start, op, test, true, false)

            monkeys.append(monkey)


    for i in range(10000):
        for monkey in monkeys:
            for j in range(len(monkey.items)):
                item = monkey.items[j]

                new = monkey.operate(item)
                new = new % (3 * 13 * 2 * 11 * 5 * 17 * 19 * 7)
                # new //= 3

                monkey.inspect_times += 1

                if monkey.testVal(new):
                    monkeys[monkey.true_target].items.append(new)
                else:
                    monkeys[monkey.false_target].items.append(new)

            monkey.items = []

    monkeys.sort(key=lambda x: x.inspect_times, reverse=True)

    business_level = monkeys[0].inspect_times * monkeys[1].inspect_times

    print(business_level)
    for monkey in monkeys:
        print(monkey)
