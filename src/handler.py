# coding:utf-8
from .settings import RoundSettings
from .judge import run_judge
from .compile import compile
from config import *
from .utils import import_data,randomize_round_id


class Handler(object):

    def __init__(self,data,data_dir,output_dir):
        # 初始化设定
        self.settings  = RoundSettings(data,data_dir,output_dir)

    #评测
    def run(self):
        # 测试数据是否正确
        data = import_data(self.settings.data_dir)
        # print(data)
        
        if data['status']!= 0:
            data['mid'] = PREPARE_JUDGE
            data["message"] = "数据列表错误"
            return data

        # for debug 输出 round dir
        # print(self.settings.round_dir)

        for_compile_data = {
               "code":self.settings.code,
               "data_dir":self.settings.data_dir,
               "round_dir":self.settings.round_dir,
               "judge_client_id":1,
               "cmp":self.settings.cmp
        }

        #groups = [run_judge.s(for_judge_data,key,val,idx)
        #                  for idx, (key, val) in enumerate(data, start=1)]

        compile_result= compile(
               self.settings.code, #code
               self.settings.data_dir,#data_dir
               self.settings.round_dir,#round_dir
               "judge_client_id",
               self.settings.cmp,
               "revert",
               self.settings.src_path,
               self.settings.compile_cmd,
               self.settings.compile_out_path,
               self.settings.compile_log_path,
               self.settings.language_settings['env']
        )
        
        # 编译失败
        if compile_result["status"] != 0 :
            compile_result["mid"] = 2
            return compile_result

        # 评测

        for_judge_data = {
                "time":self.settings.time,
                "memory":self.settings.memory,
                "output_size":self.settings.output_size,
                "judger":self.settings.judger,
                "run_cmd":self.settings.run_cmd,
                "env":self.settings.language_settings["env"],
                "rule":self.settings.language_settings["seccomp_rule"],
                "data_dir":self.settings.data_dir,
                "round_dir":self.settings.round_dir,
                "cmp":self.settings.cmp,
                "judge_client_id":"judge_client_id",
                "revert":"revert"
        }

        judge_result = []
        for idx, (input_data, output_data) in enumerate(data["result"], start=1):
            res = run_judge(for_judge_data,input_data,output_data,idx)
            judge_result.append(res)

        return judge_result

