lava = set()
neighbour_pairs = 0
with open("input.txt", "r") as input:
    for line in input:
        lava.add(pos := tuple(map(int, line.rstrip().split(","))))
        neighbour_pairs += sum(
            nb in lava
            for nb in (
                tuple(pos[i] + (j == i) * k for i in range(3))
                for j in range(3)
                for k in (-1, 1)
            )
        )
print(6 * len(lava) - 2 * neighbour_pairs)

## PART TWO
upper_limits = tuple(max(pos[i] for pos in lava) + 2 for i in range(3))
steam = set()
current = set((upper_limits,))
while current:
    steam.update(current)
    current = set(
        nb
        for nb in (
            tuple((pos[i] + (j == i) * k) % upper_limits[i] for i in range(3))
            for pos in current
            for j in range(3)
            for k in (-1, 1)
        )
        if nb not in steam and nb not in lava
    )
print(
    sum(
        nb in lava
        for nb in (
            tuple((pos[i] + (j == i) * k) % upper_limits[i] for i in range(3))
            for pos in steam
            for j in range(3)
            for k in (-1, 1)
        )
    )
)
