# 对测试的结果进行格式化输出
from config import *
from .utils import mq_emit


# 简要输出,一行
# 参数如下:
# result_arr 结果数组
# oier_name  选手名字,default=""
# idx        题目编号,default=""
def simple_print(result_arr,oier_name="",idx="",score=100):
    total_memory =0
    total_time = 0
    total_score = 0
    one_score = 0
    result_str=""

    if "status" in result_arr and result_arr["status"] != 0 :
        print(deal_wrong(result_arr))
        return
    else:
        one_score = score/len(result_arr)

    for i in result_arr:
        total_time += i["time"]
        total_memory += i["memory"]
        result_str += result_code[str(i["result"])]["short"]
        if i["result"] == 0:
            total_score += one_score

    total_memory = round(total_memory /1024,2)

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
    format_string += format_ta

    format_string += "分值: {score}"

    out = format_string.format(oier_name=oier_name,idx=idx,total_memory=total_memory,total_time=total_time,result_str=result_str,score=round(total_score,2))

    print(out)
    return out
# 详细输出,多行





def deal_wrong(result):
    mid = result["mid"]

    if mid == PREPARE_JUDGE:
        return "错误阶段:准备评测,原因:"+result["message"]
    elif mid == COMPILING:
        return "错误阶段:{},原因:{}".format("编译",result["details"])

