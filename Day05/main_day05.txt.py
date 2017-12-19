if __name__ == "__main__":

    f = open('data.txt', 'r')
    instructions = list(map(int, f.read().split(chr(10))))
    f.close()

    print(type(instructions))

    pos = 0
    t = 0
    while True:
        t = t + 1

        oldPos = pos
        pos = pos + instructions[pos]

        if pos < len(instructions):
            instructions[oldPos] = instructions[oldPos] + 1
        else:
            break



    print(t)
