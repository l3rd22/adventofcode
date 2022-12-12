def a_star(grid, start, finish):
    open_list = [dict(node=start, f=0)]
    closed_list = set()
    while open_list:
        current_node = open_list.pop((f := [n["f"] for n in open_list]).index(min(f)))
        if current_node["node"] == finish:
            path = [current_node]
            while predecessor := path[-1].get("predecessor", False):
                path.append(predecessor)
            return [node["node"] for node in path][::-1]
        closed_list.add(current_node["node"])
        for successor in get_successors(grid, current_node["node"]):
            if successor in closed_list:
                continue
            tentative_g = current_node.get("g", 0) + 1
            try:
                successor = open_list[
                    [node["node"] for node in open_list].index(successor)
                ]
            except ValueError:
                successor = dict(
                    node=successor,
                    predecessor=current_node,
                    g=tentative_g,
                    f=tentative_g + distance(successor, finish),
                )
                open_list.append(successor)
            else:
                if tentative_g >= successor.get("g", 0):
                    continue
                successor["predecessor"] = current_node
                successor["g"] = tentative_g
                successor["f"] = tentative_g + distance(successor["node"], finish)
    return None


def get_successors(grid, node):
    successors = []
    i, j = node
    for ii, jj in ((i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)):
        if ii < 0 or jj < 0:
            continue
        try:
            if grid[ii][jj] <= grid[i][j] + 1:
                successors.append((ii, jj))
        except IndexError:
            continue
    return successors


def distance(node1, node2):
    return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])
