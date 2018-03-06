# coding:utf-8

import yaml
import os
import argparse
from src.handler import Handler
from src.post import simple_print


# 命令行参数相关的设定
parser = argparse.ArgumentParser()
parser.add_argument("--src", help="源代码的路径")
parser.add_argument("--data", help="数据路径")
parser.add_argument("--memory", type=int,help="内存限制")
parser.add_argument("--time", type=int,help="时间限制")
parser.add_argument("--config", type=str,help="比较模式时,YAML配置文件的路径")
parser.add_argument("--score", type=int,default=100,help="比较模式时,YAML配置文件的路径")
args = parser.parse_args()
args_dict = args.__dict__

# 得到src 的语言类型
def get_src_lang(code_src):
    pass

# 输出评测结果
def print_judge_res():
    pass

# 处理一个评测
def single(code_src,data_dir,output_dir="output",time_limit=1,memory_limit=512,spj="fcmp2",output_size=1024,lang="cpp"):
    code = ""
    with open(code_src) as f:
        code = f.read()
    pass
    data = {
        "code":code,
        "time":time_limit,
        "memory":memory_limit,
        "lang":lang
        }
    t1 = Handler(data,data_dir,output_dir)

    # 得到结果
    res = t1.run()
    return res


# 处理比赛模式
def contest(config_path):
    if not os.path.exists(config_path):
        print("没有打到配置文件",config_path)
        exit(1)
    config_c=""
    with open(config_path) as f:
        config_c = f.read()
    config = yaml.load(config_c)

    print("====== 欢迎参加比赛: %s ======" % config["name"])

    data_base_path = config["data_base_path"]
    user_base_path = config["user_base_path"]
    problems = config["problems"]
    

    users = list(filter(lambda x:os.path.isdir(os.path.join(user_base_path,x)) ,os.listdir(user_base_path)))

    if len(users) == 0:
        print("选手目录为空:",user_base_path)
    else:
        print("参加的选手有:",",".join(users))

    ### ????? to do
    out_path = 'output'
    # 对每个选手进行测试
    for user in users:
        _path_ = os.path.join(user_base_path,user)
        print("\n\n评测代码,选手:",user)
        for problem in problems:

            code_path =  os.path.join(_path_,problem["name"]+".cpp")
            if os.path.exists(code_path):
                data = {}

                data["code_src"] = code_path

                # 数据目录 是否有参数
                data["data_dir"] = os.path.join(data_base_path,problem["name"])

                # 时间限制
                if "time" in problem:
                    data["time_limit"] = problem["time"]

                # 内存限制
                if "memory" in problem:
                    data["memory_limit"] = problem["memory"]

                # spj
                if "spj" in problem:
                    data["spj"] = problem["spj"]

                # 运行
                res = single(**data)
                _score = 100
                if "score" in problem:
                    _score = int(problem["score"])
                simple_print(res,score=_score)
            else:
                print("代码文件不存在:",problem["name"]+".cpp")

    




# 根据命令行 进行评测

# 进行single
if args_dict["config"] == None:
    data = {}

    # 数据路径是否为空
    if args_dict["src"] == None:
        pass # 本目录下查找*.py,*.cpp,*.c,*.pas
    else:
        data["code_src"] = args_dict["src"]

    # 数据目录 是否有参数
    if args_dict["data"] == None:
        pass  # 本目录下查找文件夹
    else:
        data["data_dir"] = args_dict["data"]

    # 时间限制
    if args_dict["time"] != None:
        data["time_limit"] = args_dict["time"]

    # 内存限制
    if args_dict["memory"] != None:
        data["memory_limit"] = args_dict["memory"]

    # 运行
    res = single(**data)
    simple_print(res,score=args_dict["score"])


# 进行比赛模式
else:
    contest(args_dict["config"])
