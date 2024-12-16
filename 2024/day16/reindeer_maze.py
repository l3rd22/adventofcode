#!/usr/bin/env python3


def main():
    with open("input.txt", "r") as fobj:
        maze = [line.rstrip() for line in fobj]
    nrow, ncol = (len(maze) - 1) // 2, (len(maze[0]) - 1) // 2
    INF = nrow * ncol * 1000 * 10
    vertices = {c + 1j * r: [INF, 0] for c in range(ncol) for r in range(nrow)}
    vertices[1j * (nrow - 1)] = [0, 1]
    unvisited = set(vertices)
    while unvisited:
        u, (u_d, u_dir) = min(
            ((k, vertices[k]) for k in unvisited), key=lambda v: v[1][0]
        )
        if u == (ncol - 1):
            break
        unvisited.remove(u)
        for v_dir in (1, 1j, -1, -1j):
            if (
                maze[int((2 * u + 1j + v_dir).imag)][int((2 * u + 1 + v_dir).real)]
                == "#"
            ):
                continue
            v = u + v_dir
            if v not in unvisited:
                continue
            v_d = u_d + 2 + 1000 * (v_dir != u_dir)
            if v_d < vertices[v][0]:
                vertices[v] = [v_d, v_dir]
    print(vertices[ncol - 1][0])


if __name__ == "__main__":
    main()
