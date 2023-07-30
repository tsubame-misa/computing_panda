import json
import os
import setup
import shutil

LOG = dict()
TIME = ""


def add_log(key, value):
    LOG[key] = value


def clear():
    global LOG
    LOG = dict()


def set_time(time):
    global TIME
    TIME = time


def create_log_folder():
    dir_name = setup.get_dir_name()
    path = os.getcwd()
    new_dir_path = path + "/" + dir_name

    if os.path.isdir(new_dir_path):
        return

    os.mkdir(new_dir_path)

    folders = ["log", "SGD", "best_graph"]
    for f in folders:
        new_dir_path = path + "/" + dir_name + "/" + f
        os.mkdir(new_dir_path)

    folders = ["json", "images"]
    for f in folders:
        new_dir_path = path + "/" + dir_name + "/best_graph/" + f
        os.mkdir(new_dir_path)


def create_log(_log=None, filename=""):
    dir_name = setup.get_dir_name()
    print(LOG)
    if _log == None:
        _log = LOG

    path = os.getcwd()
    with open(path + "/"+dir_name+"/log/" + filename + "-" + TIME + ".json", "w") as f:
        json.dump(_log, f)


def get_log():
    return LOG


def create_submit_data(data, filename):
    # 座標jsonの作成
    node_pos = dict()
    num2node = {v: k for k, v in data["node2num"].items()}
    for i in range(len(data["pos"])):
        node_pos[num2node[i]] = data["pos"][i]

    dir_name = setup.get_dir_name()
    path = os.getcwd()
    with open(path + "/"+dir_name+"/best_graph/json/" + filename + ".json", "w") as f:
        json.dump(node_pos, f)

    # 描画結果画像の作成
    img_path = path + "/"+dir_name+"/SGD/"+filename+"-"+data["id"]+".png"
    copy_img_path = path + "/"+dir_name + \
        "/best_graph/images/"+filename+"-"+data["id"]+".png"
    shutil.copyfile(img_path, copy_img_path)
