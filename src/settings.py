# encoding: utf-8
import os
from .languages import LANGUAGE_SETTINGS
from config import *

class RoundSettings:

    def __init__(self, data, data_dir,output_dir):
        """
        :param data: should include:
        max_time, max_sum_time, max_memory, problem_id
        lang
        code
        :param round_id: round id
        """
        # 原给 websocket 的值, 现在无用,删除
        # self.judge_client_id = data['judge_client_id']

        self.judger = "qjudge"
        if "judger" in data:
            self.judger = data["judger"]

        # 原socket emit的返回的特定值,现在无用,删除
        #self.revert = None
        #if "revert" in  data:
        #    self.revert = data["revert"]

        
        # 文件比较器
        self.cmp= 'fcmp2'
        if 'cmp' in data:
            self.cmp =data['cmp']

        self.output_size = 1024
        if "output_size" in data:
            self.output_size = data["output_size"]

        self.code = data['code']
        self.time = data['time']
        self.memory = data['memory']

        # 数据目录
        self.data_dir = data_dir

        # 执行代码的目录
        self.round_dir = output_dir

        self.language_settings = LANGUAGE_SETTINGS[data['lang']]
        # self.run_dir = self.settings.round_dir

        # Ready to make some files
        self.src_name = self.language_settings['src_name']
        self.exe_name = self.language_settings['exe_name']
        self.src_path = os.path.join(self.round_dir, self.src_name)
        self.exe_path = os.path.join(self.round_dir, self.exe_name)

        # Compilation related
        self.compile_out_path = os.path.join(self.round_dir, 'compile.out')
        self.compile_log_path = os.path.join(self.round_dir, 'compile.log')
        self.compile_cmd = self.language_settings['compile_cmd'].format(
            src_path=self.src_path,
            exe_path=self.exe_path,
        ).split(' ')

        # Running related
        self.seccomp_rule_name = self.language_settings['seccomp_rule']
        self.run_cmd = self.language_settings['exe_cmd'].format(
            exe_path=self.exe_path,
            # The following is for Java
            exe_dir=self.round_dir,
            exe_name=self.exe_name,
            max_memory=self.memory
        ).split(' ')

        # 源代码

        # OS init
        if not os.path.exists(self.data_dir): # 能不能造成自己的异常呢?
            raise FileNotFoundError
        if not os.path.exists(self.round_dir):
            os.mkdir(self.round_dir)

        # 无用
        # os.chown(self.round_dir, COMPILER_USER_UID, COMPILER_GROUP_GID)
