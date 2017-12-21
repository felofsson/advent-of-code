

if __name__ == "__main__":

    f = open('data.txt', 'r')
    instructions = f.read().split(chr(10))
    f.close()

    grand_parent = None

    # Parse the list of instructions twice
    instructions.extend(instructions)

    for line in instructions:

        parent_and_child = line.split("->")
        parent = parent_and_child[0].split(" ")[0]

        if grand_parent is None:
            grand_parent = parent

        if len(parent_and_child) > 1:
            children = list(map(lambda x: x.lstrip(), parent_and_child[1].split(",")))

            if grand_parent in children:
                grand_parent = parent

    print("grand_parent=", grand_parent)
