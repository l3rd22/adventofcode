#!/usr/bin/env python3


dictionary = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def first_digit(line, match_string=False):
    for i, char in enumerate(line):
        if char.isdigit():
            return int(char)
        if match_string:
            for key, val in dictionary.items():
                if line.startswith(key, i):
                    return val


def last_digit(line, match_string=False):
    line = line[::-1]
    for i, char in enumerate(line):
        if char.isdigit():
            return int(char)
        if match_string:
            for key, val in dictionary.items():
                if line.startswith(key[::-1], i):
                    return val


def main():
    with open("input.txt", "r") as fobj:
        calibration_values = [
            10 * first_digit(line) + last_digit(line) for line in fobj
        ]
    print(sum(calibration_values))

    with open("input.txt", "r") as fobj:
        calibration_values = [
            10 * first_digit(line, match_string=True)
            + last_digit(line, match_string=True)
            for line in fobj
        ]
    print(sum(calibration_values))


if __name__ == "__main__":
    main()
