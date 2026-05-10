import networkx as nx

def build_graph(triples):
    G = nx.DiGraph()

    for t in triples:
        G.add_edge(
            t["subject"],
            t["object"],
            relation=t["relation"],
            time=t["time"]
        )

    return G