def sgn(x):
    return (x > 0) - (x < 0)


starting_pos = (0 + 0j)
head_positions = [starting_pos]
with open("input.txt", "r") as moveset:
    for d, s in (move.rstrip().split() for move in moveset):
        direction, steps = d, int(s)
        match direction:
            case "R":
                head_positions.extend(
                    head_positions[-1] + (1 + 0j) for _ in range(steps)
                )
            case "L":
                head_positions.extend(
                    head_positions[-1] + (-1 + 0j) for _ in range(steps)
                )
            case "U":
                head_positions.extend(
                    head_positions[-1] + (0 + 1j) for _ in range(steps)
                )
            case "D":
                head_positions.extend(
                    head_positions[-1] + (0 - 1j) for _ in range(steps)
                )
knot_positions = [head_positions]
for knot_number in range(1, 10):
    knot_pos = [starting_pos]
    lead_pos = knot_positions[-1]
    for i, lead in enumerate(lead_pos[1:]):
        knot_pos.append(knot_pos[-1])
        distance = lead - knot_pos[-1]
        if abs(distance * distance.conjugate()) > 2:
            knot_pos[-1] += (sgn(distance.real) + sgn(distance.imag) * 1j)
    knot_positions.append(knot_pos)
print(len(set(knot_positions[1])))
print(len(set(knot_positions[-1])))
