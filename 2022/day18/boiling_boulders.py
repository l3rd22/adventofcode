positions = set()
neighbour_pairs = 0
with open("input.txt", "r") as input:
    for line in input:
        positions.add(pos := tuple(map(int, line.rstrip().split(","))))
        neighbour_pairs += sum(
            adj in positions
            for adj in (
                tuple(pos[i] + (j == i) * k for i in range(3))
                for j in range(3)
                for k in (-1, 1)
            )
        )
print(6 * len(positions) - 2 * neighbour_pairs)
