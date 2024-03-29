import math
from common import drawGraph,  calcDrawInfo,  initGraph, evaluation
import setup
import itertools


def sgd(graph, file_name):
    loop = setup.get_SGD_loop()
    node_len = len(graph.nodes)
    node2num = initGraph.get_node2num_memoized(graph)

    # 最短経路
    d = initGraph.get_shortest_path(graph, node_len, node2num, file_name)
    # 重み
    w = [[1]*node_len for i in range(node_len)]
    # 重み(バネの強さ)
    k = [[0]*node_len for i in range(node_len)]
    # 理想的なバネの長さ(今回はL=1のため最短経路と一致)
    l = [[0]*node_len for i in range(node_len)]

    maxd = initGraph.get_maxd(graph, file_name)
    for i in range(node_len):
        for j in range(node_len):
            if i == j:
                continue
            w[i][j] = pow(d[i][j], -2)
            l[i][j] = d[i][j]
            k[i][j] = 1/(d[i][j]*d[i][j])

    height = maxd**2
    width = maxd**2

    pos = initGraph.get_pos(node_len, width, height)

    eps = 0.1
    eta_max = 1/(min(list(itertools.chain.from_iterable(w))))
    eta_min = eps/(max(list(itertools.chain.from_iterable(w))))
    eta = eta_max
    _lamda = -1*math.log(eta_min/eta_max)/loop

    for t in range(loop):
        pair_index = initGraph.get_random_pair(node_len, loop, t)
        eta = eta_max*pow(math.e, -1*_lamda*t)

        for i, j in pair_index:
            mu = w[i][j]*eta
            if mu > 1:
                mu = 1
            rx = (calcDrawInfo.dist(pos, i, j)-d[i][j])/2 * \
                (pos[i][0]-pos[j][0])/calcDrawInfo.dist(pos, i, j)
            ry = (calcDrawInfo.dist(pos, i, j)-d[i][j])/2 * \
                (pos[i][1]-pos[j][1])/calcDrawInfo.dist(pos, i, j)

            pos[i][0] = pos[i][0]-mu*rx
            pos[i][1] = pos[i][1]-mu*ry
            pos[j][0] = pos[j][0]+mu*rx
            pos[j][1] = pos[j][1]+mu*ry

    delta = calcDrawInfo.calc_delta(pos, k, l, node_len)
    edge_score = [(d[node2num[str(u)]][node2num[str(v)]] -
                  calcDrawInfo.dist(pos, node2num[str(u)], node2num[str(v)]))**2 for u, v in graph.edges]
    drawGraph.draw_graph(graph, pos, delta, edge_score,
                         node_len, "SGD", file_name)
    score = evaluation.calc_score(graph, pos, node2num)
    _log = dict()
    _log["score"] = score
    _log["pos"] = pos
    _log["node2num"] = node2num

    return _log
