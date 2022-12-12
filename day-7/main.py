class Node:
    def __init__(self, name, is_directory, size, parent=None):
        self.name = name
        self.is_directory = is_directory
        self.size = size
        self.children = []
        self.parent = parent

def traverse(node):
    if node is None:
        return

    print(node.name, node.size, "" if node.parent is None else node.parent.name)
    for i in node.children:
        traverse(i)

def trackSize(node):
    if not node.is_directory:
        return 0

    s = 0
    if node.size >= 30000000:
        print(node.size, node.name)
        s += node.size

    for i in node.children:
        s += trackSize(i)

    return s

def trackSize2(node, tracked=None):
    if tracked is None:
        tracked = []

    if not node.is_directory:
        return 0

    tracked.append([node.name, node.size])

    for i in node.children:
        trackSize2(i, tracked)

    return tracked

def getSize(node):
    if node is None:
        return size

    s = 0
    s += node.size

    for i in node.children:
        s += getSize(i)

    return s

def setSize(node):
    if node is None or not node.is_directory:
        return

    node.size = getSize(node)
    for i in node.children:
        setSize(i)

with open("./input.txt") as file:
    fs = Node("/", True, 0)

    current = fs

    for line in file.read().split("\n"):
        if not line.startswith("$"):
            if line.startswith("dir"):
                folder = line[4:]
                current.children.append(Node(folder, True, 0, current))
            else:
                a = line.split(" ")
                file, size = a[1], int(a[0])
                current.children.append(Node(file, False, size, current))
        else:
            command = line[2:]
            if command.startswith("cd"):
                directory = command[3:]

                if directory == "..":
                    current = current.parent
                elif directory != "/":
                    current = [x for x in current.children if x.name == directory][0]

    print(getSize(fs))
    setSize(fs)

    sizes = trackSize2(fs)

    sizes = sorted(sizes, key=lambda x: x[1])

    c = 70000000 - sizes[len(sizes) - 1][1]

    print(c)
    for name, s in sizes:
        if name == "/":
            continue

        if c + s >= 30000000:
            print(str(s) + " is the size")
            break


