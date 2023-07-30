import glob
from networkx.readwrite import json_graph
import json
import setup
from algorithm import SGD
from common import drawGraph,  log
import re


def get_best_graph(logs):
    sorted_logs = sorted(logs, key=lambda x: x["score"])
    return sorted_logs[0]


def create_graph(graph, file_name):
    logs = []
    term = setup.get_term()
    for i in range(term):
        setup.init()
        setup.set_dir_name(log_file_name)
        time = setup.get_time()
        index_time = str(i) + str(time)
        drawGraph.set_time(index_time)
        _log = SGD.sgd(graph, file_name)
        _log["id"] = index_time
        logs.append(_log)
        print(index_time, _log["score"])

    best_graph = get_best_graph(logs)
    log.create_submit_data(best_graph, file_name)
    time = setup.get_time()
    log.create_log(logs, file_name)


files = glob.glob("./graph/*")
graphs = []

for filepath in files:
    graph = json_graph.node_link_graph(json.load(open(filepath)))
    file_name = re.split('[/.]', filepath)[3]
    obj = {"name": file_name, "graph": graph}
    graphs.append(obj)


sorted_graphs = sorted(graphs, key=lambda x: len(x["graph"].nodes))
log_file_name = "result"
setup.set_dir_name(log_file_name)
log.create_log_folder()

for g in sorted_graphs:
    if len(g["graph"].nodes) > 100:
        setup.set_term(1)
    else:
        setup.set_term(20)
    print(g["name"], "size", len(g["graph"].nodes))
    create_graph(g["graph"], g["name"])
    print("---------------------")
