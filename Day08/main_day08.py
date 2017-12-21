
def parse_condition(value1, condition, value2):

    if condition == ">":
        return value1 > value2
    elif condition == "<":
        return value1 < value2
    elif condition == "!=":
        return value1 != value2
    elif condition == "<=":
        return value1 <= value2
    elif condition == ">=":
        return value1 >= value2
    elif condition == "==":
        return value1 == value2
    else:
        print("lwelwe")


def compute_operation(value1, value2, operation):

    if operation == "inc":
        return value1+value2
    elif operation == "dec":
        return value1 - value2
    else:
        print("lwelwlele")


if __name__ == "__main__":

    f = open('data.txt', 'r')
    instructions = f.read().split(chr(10))
    f.close()

    register = {}

    for line in instructions:

        operand1, operation1, value1 = line.split("if")[0].rstrip().split(" ")
        operand2, condition, value2 = line.split("if")[1].lstrip().split(" ")

        for operand in [operand1, operand2]:
            if operand not in register:
                register[operand] = 0

        if parse_condition(register[operand2], condition, int(value2)):

            register[operand1] = compute_operation(register[operand1], int(value1), operation1)

    print(register[max(register, key=register.get)])
