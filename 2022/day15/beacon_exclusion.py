sensors = []
beacons = set()
y0 = 2_000_000
with open("input.txt", "r") as readings:
    for line in readings:
        sx, sy, bx, by = map(
            int,
            (
                line.replace("=", ",").replace(":", ",").split(",")[i]
                for i in range(1, 8, 2)
            ),
        )
        sensors.append((sx, sy, abs(sx - bx) + abs(sy - by)))
        beacons.add((bx, by))
blocked = set()
for s in sensors:
    for i in range(-(dx := s[2] - abs(s[1] - y0)), dx + 1):
        blocked.add(s[0] + i)
print(len(blocked) - sum(b[1] == y0 for b in beacons))

# doesn't even work for example_input.txt...
enclosing_pairs = []
for i, s1 in enumerate(sensors[:-1], 1):
    for s2 in sensors[i:]:
        if (abs(s1[0] - s2[0]) + abs(s1[1] - s2[1])) == (s1[2] + s2[2] + 2):
            enclosing_pairs.append((s1, s2))
b_ = [0, 0]
for (s1, s2) in enclosing_pairs:
    s1_ = (s1[0] + s1[1], s1[0] - s1[1], s1[2])
    s2_ = (s2[0] + s2[1], s2[0] - s2[1], s2[2])
    if abs(s1_[0] - s2_[0]) > abs(s1_[1] - s2_[1]):
        s1_, s2_ = sorted([s1_, s2_], key=lambda x: x[0])
        b_[0] = (s1_[0] + s1_[2] + s2_[0] - s2_[2]) // 2
    else:
        s1_, s2_ = sorted([s1_, s2_], key=lambda x: x[1])
        b_[1] = (s1_[1] + s1_[2] + s2_[1] - s2_[2]) // 2
b = [(b_[0] + b_[1]) // 2, (b_[0] - b_[1]) // 2]
print(4_000_000 * b[0] + b[1])
