import itertools
import math
import networkx as nx
import setup


def calc_score(graph, pos, node2num):
    UNIT_EDGE_LENGTH = setup.get_edge_width()
    d = dict(nx.all_pairs_dijkstra_path_length(
        graph, weight=lambda u, v, e: UNIT_EDGE_LENGTH))

    s = 0
    for u, v in itertools.combinations(graph.nodes, 2):
        _u = node2num[str(u)]
        _v = node2num[str(v)]
        s += (math.hypot(pos[_u][0] - pos[_v][0], pos[_u]
                         [1] - pos[_v][0]) - d[u][v]) ** 2 / d[u][v] ** 2

    return s
