#!/usr/bin/env python3

from queue import PriorityQueue
from dataclasses import dataclass, field
from typing import Any


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any = field(compare=False)


def neighbors(vertex):
    for dir_ in (1, 1j, -1, -1j):
        yield vertex + dir_


def dijkstra(vertices, start, target):
    INF = 1_000_000_000
    dist = {vertex: INF for vertex in vertices}
    dist[start] = 0
    # prev = {}
    pq = PriorityQueue()
    pq.put(PrioritizedItem(0, start))
    unvisited = set(dist)
    while unvisited:
        mindist = pq.get()
        udist, u = mindist.priority, mindist.item
        if u == target:
            break
        unvisited.remove(u)
        for v in neighbors(u):
            if v not in unvisited:
                continue
            vdist = udist + 1
            if vdist < dist[v]:
                dist[v] = vdist
                pq.put(PrioritizedItem(vdist, v))
                # prev[v] = u
    return dist[target]


def main() -> None:
    corrupted = set()
    with open("input.txt", "r") as fobj:
        for _ in range(1024):  # example: 12
            x, y = map(int, next(fobj).split(","))
            corrupted.add(x + 1j * y)
    upper_limit = 70  # example: 6
    memory = filter(
        lambda x: x not in corrupted,
        (x + 1j * y for y in range(upper_limit + 1) for x in range(upper_limit + 1)),
    )
    print(dijkstra(memory, 0j, upper_limit + 1j * upper_limit))

    def connect_clusters(vertex):
        cluster = set()
        stack = [vertex]
        left, right = False, False
        while stack:
            vert = stack.pop()
            cluster.add(vert)
            for dir_ in (1, 1 + 1j, 1j, -1 + 1j, -1, -1 - 1j, -1j, 1 - 1j):
                neighbor = vert + dir_
                if neighbor in cluster or neighbor not in clusters["all"]:
                    continue
                for i, other in enumerate(clusters["free"]):
                    if neighbor in other:
                        cluster.update(clusters["free"].pop(i))
                if (
                    neighbor in clusters["left"]
                    or int(neighbor.real) == 0
                    or int(neighbor.imag) == upper_limit
                ):
                    left = True
                    clusters["left"].update(cluster)
                    cluster = clusters["left"]
                if (
                    neighbor in clusters["right"]
                    or int(neighbor.real) == upper_limit
                    or int(neighbor.imag) == 0
                ):
                    right = True
                    clusters["right"].update(cluster)
                    cluster = clusters["right"]
                if neighbor not in cluster:
                    stack.append(neighbor)
        if left and right:
            return True
        if not left and not right:
            clusters["free"].append(cluster)
        return False

    clusters = {"left": set(), "right": set(), "free": [], "all": set()}
    with open("input.txt", "r") as fobj:
        for i, line in enumerate(fobj):
            x, y = map(int, line.split(","))
            clusters["all"].add(x + 1j * y)
            if connect_clusters(x + 1j * y):
                print(f"{x},{y}")
                break


if __name__ == "__main__":
    main()
