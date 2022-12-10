(X := [1]).extend(
    xi
    for x in (
        (X[-1],) if instr.startswith("noop") else (X[-1], X[-1] + int(instr[5:]))
        for instr in open("input.txt", "r")
    )
    for xi in x
)
print(sum(X[i - 1] * i for i in range(20, 221, 40)))
print(
    "".join(
        ["", "\n"][cycle % 40 == 0] + [" ", "█"][cycle % 40 - sprite_pos in (-1, 0, 1)]
        for cycle, sprite_pos in enumerate(X[:-1])
    )
)
