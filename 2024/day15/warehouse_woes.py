#!/usr/bin/env python3


def print_warehouse(warehouse):
    ncol = max(int(w.real) for w in warehouse) + 1
    nrow = max(int(w.imag) for w in warehouse) + 1
    print(
        "\n".join(
            "".join(warehouse[c + 1j * r] for c in range(ncol)) for r in range(nrow)
        )
        + "\033[A" * (nrow),
        end="\r",
    )


def move(warehouse, pos, dir_):
    newpos = pos + dir_
    if warehouse[newpos] == "#":
        return False
    if warehouse[newpos] == "O":
        move(warehouse, newpos, dir_)
    if warehouse[newpos] == ".":
        warehouse[newpos] = warehouse[pos]
        warehouse[pos] = "."
        return True
    return False


def main():
    with open("input.txt", "r") as fobj:
        warehouse_, moves = fobj.read().split("\n\n")
    moves = moves.replace("\n", "")
    direction = {"^": -1j, ">": 1, "v": 1j, "<": -1}
    warehouse = {
        (x + 1j * y): c
        for y, line in enumerate(warehouse_.split("\n"))
        for x, c in enumerate(line)
    }
    robot = list(warehouse.keys())[list(warehouse.values()).index("@")]
    for m in moves:
        dir_ = direction[m]
        robot += move(warehouse, robot, dir_) * dir_
        # print_warehouse(warehouse)
    print(
        sum(int(p.real) + 100 * int(p.imag) for p in warehouse if warehouse[p] == "O")
    )


if __name__ == "__main__":
    main()
