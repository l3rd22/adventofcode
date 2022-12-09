tree_heights = [list(map(int, list(row))) for row in open("input.txt", "r").read().splitlines()]
print(
    sum(
        sum(h or v for h, v in zip(hvis, vvis))
        for hvis, vvis in zip(
            (
                (
                    (tree > max(row[:i])) or (tree > max(row[i + 1 :]))
                    for i, tree in enumerate(row[1:-1], 1)
                )
                for row in tree_heights[1:-1]
            ),
            map(
                list,
                zip(
                    *(
                        [
                            (tree > max(col[:i])) or (tree > max(col[i + 1 :]))
                            for i, tree in enumerate(col[1:-1], 1)
                        ]
                        for col in list(map(list, zip(*tree_heights)))[1:-1]
                    )
                ),
            ),
        )
    )
    + 2 * (len(tree_heights) + len(tree_heights[0]) - 2)
)
print(
    max(
        max(h * v for h, v in zip(hss, vss))
        for hss, vss in zip(
            (
                [
                    next((j for j, t in enumerate(row[:i][::-1], 1) if t >= tree), i)
                    * next(
                        (j for j, t in enumerate(row[i + 1 :], 1) if t >= tree),
                        len(row[i + 1 :]),
                    )
                    for i, tree in enumerate(row)
                ]
                for row in tree_heights
            ),
            map(
                list,
                zip(
                    *(
                        [
                            next(
                                (
                                    j
                                    for j, t in enumerate(col[:i][::-1], 1)
                                    if t >= tree
                                ),
                                i,
                            )
                            * next(
                                (j for j, t in enumerate(col[i + 1 :], 1) if t >= tree),
                                len(col[i + 1 :]),
                            )
                            for i, tree in enumerate(col)
                        ]
                        for col in map(list, zip(*tree_heights))
                    )
                ),
            ),
        )
    )
)
