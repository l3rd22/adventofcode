#!/usr/bin/env python3

import numpy as np


def main():
    with open("input.txt", "r") as fobj:
        data = [[int(id_) for id_ in line.split()] for line in fobj]
    list1, list2 = np.array(data).T
    print(np.sum(np.abs(np.sort(list1) - np.sort(list2))))

    similarity_score = 0
    for i in list1:
        similarity_score += i * np.sum(i == list2)
    print(similarity_score)


if __name__ == "__main__":
    main()
