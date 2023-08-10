import matplotlib.pyplot as plt
import networkx as nx
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import re
import setup


list_colors = px.colors.sequential.Plasma
IMAGE_PATH = []
TIME = ""


def set_time(time):
    global TIME
    TIME = time


def clear():
    global IMAGE_PATH, TIME
    IMAGE_PATH = []
    TIME = ""


def get_dir():
    cwd = os.getcwd()
    return cwd


def create_and_save_graph(graph, pos, node_color, edge_color, alg_dir_name, name=""):
    G = nx.DiGraph()

    G.add_nodes_from(graph.nodes)
    G.add_edges_from(graph.edges)

    plt.figure(figsize=(12, 12))
    nx.draw_networkx(G, pos, False, with_labels=False,
                     node_color=node_color, edge_color=edge_color, node_size=2, linewidths=0.5, label=None)

    dir_name = setup.get_dir_name()

    img_path = get_dir()+'/'+dir_name+'/' + alg_dir_name + '/' + \
        str(name) + '-' + TIME + '.png'
    plt.savefig(img_path)
    IMAGE_PATH.append(img_path)

    plt.clf()
    plt.close()


def get_color(delta, node_len):
    color = []
    for i in range(node_len):
        color.append(list_colors[0])
        continue
        c_idx = int(delta01[i]*10)
        if c_idx >= len(list_colors):
            c_idx = len(list_colors)-1
        color.append(list_colors[c_idx])
    return color


def get_graph_color(graph):
    color = []
    for i in range(len(graph.nodes)):
        color.append(list_colors[graph.nodes[i]["tier"]*3])
    return color


def convert_graph_dict(nodes, pos):
    dict_pos = {}
    cnt = 0
    for node in nodes:
        dict_pos[node] = pos[cnt]
        cnt += 1
    return dict_pos


def draw_graph(graph, pos, delta, edge_score, node_len, dir_name, file_name=""):
    node_color = get_color(delta, node_len)
    edge_color = get_color(edge_score, node_len)
    # グラフ描画
    dict_pos = convert_graph_dict(graph.nodes, pos)
    create_and_save_graph(graph, dict_pos,  node_color, edge_color,
                          dir_name, file_name)
