import networkx as nx

def get_paths(G, start, depth=2):
    paths = nx.single_source_shortest_path(G, start, cutoff=depth)

    return [p for p in paths.values() if len(p) > 1]

def format_paths(G, paths):
    context = ""

    for path in paths:
        for i in range(len(path) - 1):
            edge = G[path[i]][path[i + 1]]
            context += f"{path[i]} --{edge['relation']}--> {path[i+1]} ({edge['time']})\n"

    return context