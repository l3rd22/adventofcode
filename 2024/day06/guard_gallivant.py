#!/usr/bin/env python3


def patrol(map_, starting_pos, direction):
    ncols = map_.index("\n") + 1
    turn = {-ncols: 1, 1: ncols, ncols: -1, -1: -ncols}
    positions = [starting_pos]
    visited = {(starting_pos, direction)}
    while True:
        path = map_[starting_pos::direction].split("\n")[0].split("#")
        new_positions = [starting_pos + i * direction for i in range(1, len(path[0]))]
        positions.extend(new_positions)
        for pos in new_positions:
            if (pos, direction) in visited:
                return positions, False
            visited.add((pos, direction))
        if len(path) == 1:
            return positions, True
        starting_pos = positions[-1]
        direction = turn[direction]


def main():
    with open("input.txt", "r") as fobj:
        lab = fobj.read()
    up = -(lab.index("\n") + 1)
    positions, _ = patrol(lab, lab.index("^"), up)
    print(len(set(positions)))

    obstacles = set()
    tried = set()
    for pos, next_pos in zip(positions[:-1], positions[1:]):
        if next_pos in tried:
            continue
        tried.add(next_pos)
        new_lab = lab[:next_pos] + "#" + lab[next_pos + 1 :]
        if not patrol(new_lab, pos, (next_pos - pos))[1]:
            obstacles.add(next_pos)
    obstacles.discard(lab.index("^"))
    print(len(obstacles))


if __name__ == "__main__":
    main()
