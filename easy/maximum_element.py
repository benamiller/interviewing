def getMax(operations):
    stack = []
    max_values = [0]
    result = []
    print(operations)

    for operation in operations:
        command = operation.split(" ")
        if len(command) == 2 and command[0] == "1":
            number = int(command[1])
            stack.append(number)
            if number >= max_values[-1]:
                max_values.append(number)
        elif command[0] == "2" and stack:
            popped = stack.pop()
            if popped == max_values[-1]:
                max_values.pop()
        elif command[0] == "3":
            result.append(max_values[-1])

    return result


if __name__ == "__main__":
    n = int(input().strip())

    operations = []

    for _ in range(n):
        operation_item = input()
        operations.append(operation_item)

    print(getMax(operations))
