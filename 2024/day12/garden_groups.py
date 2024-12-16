#!/usr/bin/env python3


def main():
    plots = {}
    with open("input.txt", "r") as fobj:
        for r, line in enumerate(fobj):
            for c, plant in enumerate(line.rstrip()):
                plots[c + 1j * r] = plant

    unvisited = set(plots)
    regions = []
    while unvisited:
        s = next(iter(unvisited))
        plant = plots[s]
        stack = [s]

        region = set()
        area = 0
        perimeter = 0
        while stack:
            s = stack.pop()
            if s in region:
                perimeter -= 2
                continue
            if plots[s] != plant:
                continue
            region.add(s)
            area += 1
            perimeter += 4
            for d in (1, 1j, -1, -1j):
                if s + d in unvisited:
                    if s + d not in stack:
                        stack.append(s + d)
        regions.append((region, area, perimeter))
        unvisited -= region
    print(sum(r[1] * r[2] for r in regions))


if __name__ == "__main__":
    main()
