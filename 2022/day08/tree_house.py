with open("input.txt", "r") as forest:
    tree_heights = [list(map(int, list(row.rstrip("\n")))) for row in forest]
horizontal_visibility = [
    [
        (tree > max(row[:i])) or (tree > max(row[i + 1 :]))
        for i, tree in enumerate(row[1:-1], 1)
    ]
    for row in tree_heights[1:-1]
]
vertical_visibility = [
    [
        (tree > max(col[:i])) or (tree > max(col[i + 1 :]))
        for i, tree in enumerate(col[1:-1], 1)
    ]
    for col in list(map(list, zip(*tree_heights)))[1:-1]
]
vertical_visibility = list(map(list, zip(*vertical_visibility)))
print(
    sum(
        sum(h or v for h, v in zip(hvis, vvis))
        for hvis, vvis in zip(horizontal_visibility, vertical_visibility)
    )
    + 2 * (len(tree_heights) + len(tree_heights[0]) - 2)
)

## PART TWO
horizontal_scenic_score = [
    [
        next((j for j, t in enumerate(row[:i][::-1], 1) if t >= tree), i)
        * next(
            (j for j, t in enumerate(row[i + 1 :], 1) if t >= tree), len(row[i + 1 :])
        )
        for i, tree in enumerate(row)
    ]
    for row in tree_heights
]
vertical_scenic_score = [
    [
        next((j for j, t in enumerate(col[:i][::-1], 1) if t >= tree), i)
        * next(
            (j for j, t in enumerate(col[i + 1 :], 1) if t >= tree), len(col[i + 1 :])
        )
        for i, tree in enumerate(col)
    ]
    for col in map(list, zip(*tree_heights))
]
vertical_scenic_score = list(map(list, zip(*vertical_scenic_score)))
print(
    max(
        max(h * v for h, v in zip(hss, vss))
        for hss, vss in zip(horizontal_scenic_score, vertical_scenic_score)
    )
)
