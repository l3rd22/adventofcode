from copy import deepcopy


def remove_nodes(graph, nodes):
    graph = deepcopy(graph)
    for node in nodes:
        node_ = graph.pop(node)
        for nb1, dist1 in node_["neighbors"].items():
            graph[nb1]["neighbors"].pop(node)
            for nb2, dist2 in node_["neighbors"].items():
                if nb1 == nb2:
                    continue
                graph[nb1]["neighbors"][nb2] = min(
                    (graph[nb1]["neighbors"].get(nb2, 100), dist1 + dist2)
                )
    return graph


def get_paths(graph, start_node, remaining_time):
    if not graph:
        return [], []

    opened_valves = []
    released_pressure = []

    opened_valves.append([start_node])
    released_pressure.append(
        add_rp := graph[start_node]["flow_rate"] * (remaining_time - 1)
    )
    updated_graph = remove_nodes(graph, (start_node,))
    ov, rp = [], 0
    for next_node, dist in graph[start_node]["neighbors"].items():
        if dist >= remaining_time - 1 - 2:
            continue
        ov_, rp_ = get_paths(updated_graph, next_node, remaining_time - 1 - dist)
        if rp_ == []:
            continue
        if (rp_max := max(rp_)) > rp:
            rp = rp_max
            ov = ov_[rp_.index(rp_max)]
    del updated_graph
    if ov != []:
        opened_valves.append([start_node])
        opened_valves[-1].extend(ov)
        released_pressure.append(add_rp + rp)

    ov, rp = [], 0
    for next_node, dist in graph[start_node]["neighbors"].items():
        if dist >= remaining_time - 2:
            continue
        ov_, rp_ = get_paths(graph, next_node, remaining_time - dist)
        if rp_ == []:
            continue
        if (rp_max := max(rp_)) > rp:
            rp = rp_max
            ov = ov_[rp_.index(rp_max)]
    if ov != []:
        opened_valves.append(ov)
        released_pressure.append(rp)

    return opened_valves, released_pressure


graph = {}
with open("example_input.txt", "r") as input:
    for line in (
        line.rstrip().replace(";", "").replace("=", " ").split(" ") for line in input
    ):
        graph[line[1]] = {
            "flow_rate": int(line[5]),
            "neighbors": {nb.rstrip(","): 1 for nb in line[10:]},
        }
graph = remove_nodes(
    graph, (n for n in graph if n != "AA" and graph[n]["flow_rate"] == 0)
)
start_nodes, distances = zip(*graph["AA"]["neighbors"].items())
graph = remove_nodes(graph, ("AA",))
for sn, dist in zip(start_nodes, distances):
    print(get_paths(graph, start_node=sn, remaining_time=30 - dist))
