X = [1]
with open("input.txt", "r") as instructions:
    for instruction in instructions:
        X.append(X[-1])
        if instruction.startswith("addx"):
            X.append(X[-1] + int(instruction[5:]))
print(sum(X[i - 1] * i for i in range(20, 221, 40)))
