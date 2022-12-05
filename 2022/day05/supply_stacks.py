with open("input.txt", "r") as procedure:
    picture = []
    for line in procedure:
        if not line.rstrip("\n"):
            break
        picture.append(line.rstrip("\n"))
    stack_numbers = picture.pop()
    amount_stacks = int(stack_numbers.split()[-1])
    picture.reverse()

    stacks = []
    for s in range(amount_stacks):
        stacks.append([])
        for row in picture:
            crate = row[stack_numbers.index(str(s + 1))]
            if crate == " ":
                break
            stacks[s].append(crate)

    for instruction in procedure:
        move, from_, to = [int(instruction.rstrip().split()[idx]) for idx in (1, 3, 5)]
        for m in range(move):
            stacks[to - 1].append(stacks[from_ - 1].pop())
    
    print("".join([stack[-1] for stack in stacks]))
