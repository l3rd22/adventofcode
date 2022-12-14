rock_paths = []
with open("input.txt", "r") as scan:
    for line in (l.rstrip("\n").split(" -> ") for l in scan):
        rock_paths.append([tuple(map(int, xy.split(","))) for xy in line])
rock_coords = set()
for path in rock_paths:
    for (x1, y1), (x2, y2) in zip(path[:-1], path[1:]):
        rock_coords.update(
            (x + 1j * y)
            for x in (lambda s, e: range(s, e + 1))(*sorted([x1, x2]))
            for y in (lambda s, e: range(s, e + 1))(*sorted([y1, y2]))
        )
rock_bottom = max(r.imag for r in rock_coords)
sand_coords = set()
sand_pos = 500
while 500 not in sand_coords:
    if sand_pos.imag > rock_bottom:
        ## part one
        # break
        ## part two
        sand_coords.add(sand_pos)
        sand_pos = 500
    elif (next_pos := sand_pos + 1j) not in rock_coords | sand_coords:
        sand_pos = next_pos
        continue
    elif (next_pos := sand_pos - 1 + 1j) not in rock_coords | sand_coords:
        sand_pos = next_pos
        continue
    elif (next_pos := sand_pos + 1 + 1j) not in rock_coords | sand_coords:
        sand_pos = next_pos
        continue
    else:
        sand_coords.add(sand_pos)
        sand_pos = 500
print(len(sand_coords))
