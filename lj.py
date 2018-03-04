# coding:utf-8
import argparse
from src.handler import Handler
from src.post import simple_print


# 命令行参数相关的设定
parser = argparse.ArgumentParser()
parser.add_argument("--src", help="源代码的路径")
parser.add_argument("--data", help="数据路径")
parser.add_argument("--memory", type=int,help="内存限制")
parser.add_argument("--time", type=int,help="时间限制")
parser.add_argument("--config", type=int,help="比较模式时,YAML配置文件的路径")
args = parser.parse_args()
args_dict = args.__dict__

# 得到src 的语言类型
def get_src_lang(code_src):
    pass

# 输出评测结果
def print_judge_res():
    pass

# 处理一个评测
def singe(code_src,data_dir,output_dir="output",time_limit=1,memory_limit=512,spj="fcmp2",output_size=1024,lang="cpp"):
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
def contest():
    pass


print(args)
print(args.__dict__)


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
    res = singe(**data)
    simple_print(res)


# 进行比赛模式
else:
    contest()
