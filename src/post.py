# 对测试的结果进行格式化输出
from config import *
from .utils import mq_emit


# 简要输出,一行
# 参数如下:
# result_arr 结果数组
# oier_name  选手名字,default=""
# idx        题目编号,default=""
def simple_print(result_arr,oier_name="",idx=""):
    total_memory =0
    total_time = 0
    result_str=""
    for i in result_arr:
        total_time += i["time"]
        total_memory += i["memory"]
        result_str += result_code[str(i["result"])]["short"]

    total_memory = total_memory /1024

    format_string = ""
    format_ta = "    "
    if len(oier_name) > 0:
        format_string +="{oier_name:>5}"
        format_string += format_ta

    if len(idx) > 0:
        format_string +="编号:{idx:>2}"
        format_string += format_ta
    
    format_string += "总时间:{total_time:>5}s"
    format_string += format_ta

    format_string += "总内存:{total_memory:>5}mb"
    format_string += format_ta

    format_string += "结果: {result_str}"

    out = format_string.format(oier_name=oier_name,idx=idx,total_memory=total_memory,total_time=total_time,result_str=result_str)

    print(out)
    return out
# 详细输出,多行

