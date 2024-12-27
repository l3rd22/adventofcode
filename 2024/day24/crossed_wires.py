#!/usr/bin/env python3

from operator import and_, or_, xor


def main() -> None:
    wires = {}
    gates = {}
    ops = {"AND": and_, "OR": or_, "XOR": xor}
    with open("input.txt", "r") as fobj:
        for line in fobj:
            if line == "\n":
                break
            wire, in_ = line.split(": ")
            wires[wire] = int(in_)
        for line in fobj:
            in1, op, in2, _, out = line.rstrip().split(" ")
            gates[out] = (op, in1, in2)

    def sim_wire(wire):
        if wire not in wires:
            op, in1, in2 = gates[wire]
            wires[wire] = ops[op](sim_wire(in1), sim_wire(in2))
        return wires[wire]

    output = 0
    for wire in filter(lambda w: w.startswith("z"), gates):
        output |= sim_wire(wire) << int(wire[1:])
    print(output)


if __name__ == "__main__":
    main()
