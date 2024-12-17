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
    if warehouse[newpos] in "[]":
        if dir_ in (1, -1):
            move(warehouse, newpos, dir_)
        elif not move_multi(
            warehouse, [newpos, newpos + {"[": 1, "]": -1}[warehouse[newpos]]], dir_
        ):
            return False
    if warehouse[newpos] == ".":
        warehouse[newpos] = warehouse[pos]
        warehouse[pos] = "."
        return True
    return False


def move_multi(warehouse, pos, dir_):
    newpos = [p + dir_ for p in pos]
    if any(warehouse[p] == "#" for p in newpos):
        return False
    boxes = [np for np in newpos if warehouse[np] in "[]"]
    for b in boxes:
        if warehouse[b] == "[" and (b + 1) not in boxes:
            boxes.append(b + 1)
        if warehouse[b] == "]" and (b - 1) not in boxes:
            boxes.append(b - 1)
    if boxes:
        move_multi(warehouse, boxes, dir_)
    if all(warehouse[p] == "." for p in newpos):
        for np, p in zip(newpos, pos):
            warehouse[np] = warehouse[p]
            warehouse[p] = "."
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

    warehouse = {
        (2 * x + xi + 1j * y): c
        for y, line in enumerate(warehouse_.split("\n"))
        for x, char in enumerate(line)
        for xi, c in enumerate({"#": "##", "O": "[]", ".": "..", "@": "@."}[char])
    }
    robot = list(warehouse.keys())[list(warehouse.values()).index("@")]
    for m in moves:
        dir_ = direction[m]
        robot += move(warehouse, robot, dir_) * dir_
        # print_warehouse(warehouse)
    print(
        sum(int(p.real) + 100 * int(p.imag) for p in warehouse if warehouse[p] == "[")
    )


if __name__ == "__main__":
    main()
