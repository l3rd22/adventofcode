#!/usr/bin/env python3


def main() -> None:
    connections = {}
    with open("input.txt", "r") as fobj:
        for line in fobj:
            comp1, comp2 = sorted(line.rstrip().split("-"))
            connections.setdefault(comp1, set()).add(comp2)

    def get_groups(group, comps):
        newgroups = []
        for c in comps:
            newgroups.append((*group, c))
            linked = connections.get(c, set())
            newgroups.extend(get_groups(newgroups[-1], comps & linked))
        return newgroups

    groups = []
    for comp, linked in connections.items():
        for comp2 in linked:
            groups.extend(
                get_groups((comp, comp2), connections.get(comp2, set()) & linked)
            )
    print(
        len(
            list(
                filter(
                    lambda t: len(t) == 3 and any(c.startswith("t") for c in t), groups
                )
            )
        )
    )
    print(",".join(max(groups, key=lambda g: len(g))))


if __name__ == "__main__":
    main()
