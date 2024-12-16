#!/usr/bin/env python3

import re


def variance(samples):
    mean = sum(samples) / len(samples)
    return sum((xi - mean) ** 2 for xi in samples) / len(samples)


def main():
    with open("input.txt", "r") as fobj:
        robots = re.findall(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", fobj.read())
    positions = [tuple(map(int, r[:2])) for r in robots]
    velocities = [tuple(map(int, r[2:])) for r in robots]
    width, height = 101, 103  # example: 11, 7
    quadrants = [[0, 0], [0, 0]]
    for p, v in zip(positions, velocities):
        x = (p[0] + 100 * v[0]) % width
        y = (p[1] + 100 * v[1]) % height
        if x == width // 2 or y == height // 2:
            continue
        quadrants[x > width // 2][y > height // 2] += 1
    print(quadrants[0][0] * quadrants[0][1] * quadrants[1][0] * quadrants[1][1])

    var_x = [
        variance([(p[0] + i * v[0]) % width for p, v in zip(positions, velocities)])
        for i in range(width)
    ]
    var_y = [
        variance([(p[1] + i * v[1]) % height for p, v in zip(positions, velocities)])
        for i in range(height)
    ]
    ax = min(enumerate(var_x), key=lambda x: x[1])[0]
    ay = min(enumerate(var_y), key=lambda x: x[1])[0]
    t = (ax * height * pow(height, -1, width) + ay * width * pow(width, -1, height)) % (
        width * height
    )
    print(t)

    restroom = [["."] * width for _ in range(height)]
    for p, v in zip(positions, velocities):
        restroom[(p[1] + t * v[1]) % height][(p[0] + t * v[0]) % width] = "#"
    print("\n".join("".join(row) for row in restroom))


if __name__ == "__main__":
    main()
