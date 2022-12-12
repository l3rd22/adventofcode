from path_finding import a_star


with open("input.txt", "r") as height_map:
    height_map = [list(row.rstrip().encode("ascii")) for row in height_map]
start = next(
    (i, row.index(ord("S"))) for i, row in enumerate(height_map) if ord("S") in row
)
height_map[start[0]][start[1]] = ord("a")
finish = next(
    (i, row.index(ord("E"))) for i, row in enumerate(height_map) if ord("E") in row
)
height_map[finish[0]][finish[1]] = ord("z")
print(len(a_star(height_map, start, finish)) - 1)
starting_squares = (
    (i, row.index(ord("a"))) for i, row in enumerate(height_map) if ord("a") in row
)
print(
    min(len(a_star(height_map, start_, finish)) for start_ in starting_squares) - 1
)
