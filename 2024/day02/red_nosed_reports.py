#!/usr/bin/env python3

import numpy as np


def safe(report):
    differences = report[1:] - report[:-1]
    return (np.all(differences <= 3) & np.all(differences >= 1)) | (
        np.all(differences >= -3) & np.all(differences <= -1)
    )


def safe_problem_dampener(report):
    for i in range(len(report)):
        report_dampened = np.concatenate((report[:i], report[i + 1 :]))
        if safe(report_dampened):
            return True
    return False


def main():
    with open("input.txt", "r") as fobj:
        reports = [np.array(list(map(int, levels.split(" ")))) for levels in fobj]
    print(np.sum([safe(report) for report in reports]))
    print(np.sum([safe_problem_dampener(report) for report in reports]))


if __name__ == "__main__":
    main()
