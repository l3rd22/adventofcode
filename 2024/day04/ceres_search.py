#!/usr/bin/env python3

import re


def main():
    with open("input.txt", "r") as fobj:
        word_search = fobj.read()
    ncols = word_search.index("\n")
    patterns = (
        "XMAS",
        "SAMX",
        f"X(?=(?:.|\n){{{ncols}}}M(?:.|\n){{{ncols}}}A(?:.|\n){{{ncols}}}S)",
        f"S(?=(?:.|\n){{{ncols}}}A(?:.|\n){{{ncols}}}M(?:.|\n){{{ncols}}}X)",
        f"X(?=[^\n](?:.|\n){{{ncols}}}M[^\n](?:.|\n){{{ncols}}}A[^\n](?:.|\n){{{ncols}}}S)",
        f"S(?=[^\n](?:.|\n){{{ncols}}}A[^\n](?:.|\n){{{ncols}}}M[^\n](?:.|\n){{{ncols}}}X)",
        f"X(?=(?:.|\n){{{ncols - 1}}}M[^\n](?:.|\n){{{ncols - 2}}}A[^\n](?:.|\n){{{ncols - 2}}}S[^\n])",
        f"S(?=(?:.|\n){{{ncols - 1}}}A[^\n](?:.|\n){{{ncols - 2}}}M[^\n](?:.|\n){{{ncols - 2}}}X[^\n])",
    )
    matches = [re.findall(pattern, word_search) for pattern in patterns]
    print(sum([len(match) for match in matches]))

    xmas_patterns = (
        f"M(?=.M(?:.|\n){{{ncols - 1}}}A(?:.|\n){{{ncols - 1}}}S.S)",
        f"M(?=.S(?:.|\n){{{ncols - 1}}}A(?:.|\n){{{ncols - 1}}}M.S)",
        f"S(?=.M(?:.|\n){{{ncols - 1}}}A(?:.|\n){{{ncols - 1}}}S.M)",
        f"S(?=.S(?:.|\n){{{ncols - 1}}}A(?:.|\n){{{ncols - 1}}}M.M)",
    )
    xmas_matches = [re.findall(pattern, word_search) for pattern in xmas_patterns]
    print(sum([len(match) for match in xmas_matches]))


if __name__ == "__main__":
    main()
