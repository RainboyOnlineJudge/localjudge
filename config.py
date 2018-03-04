from multiprocessing import cpu_count

import grp
import os
import pwd

# Judge server directories

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TESTLIB_BUILD_DIR = '/judge/checker'
JUDGE_BASE_DIR = '/judge_server'
JUDGE_BASE_DIR_PAST = '/judge_server_past'

ROUND_DIR = os.path.join(JUDGE_BASE_DIR, 'round')
DATA_DIR = os.path.join(JUDGE_BASE_DIR, 'data')
TMP_DIR = os.path.join(JUDGE_BASE_DIR, 'tmp')

RUN_USER_UID = pwd.getpwnam("nobody").pw_uid
RUN_GROUP_GID = grp.getgrnam("nogroup").gr_gid

COMPILER_USER_UID = -1
COMPILER_GROUP_GID = -1

# Important! Code meaning!
# ERROR_CODE < 0: FORGIVEN
WRONG_ANSWER = -1
ACCEPTED = 0
# ERROR_CODE > 0: TERMINATION ERROR
CPU_TIME_LIMIT_EXCEEDED = 1
REAL_TIME_LIMIT_EXCEEDED = 2
MEMORY_LIMIT_EXCEEDED = 3
RUNTIME_ERROR = 4
SYSTEM_ERROR = 5
COMPILE_ERROR = 6
IDLENESS_LIMIT_EXCEEDED = 7
SUM_TIME_LIMIT_EXCEEDED = 8

# 结果对应的描述
result_code = {
        "-1":{ "long":"WRONG_ANSWER", "short":"W" },
        "0":{  "long":"ACCEPTED",                "short":"A"},
        "1":{  "long":"CPU_TIME_LIMIT_EXCEEDED", "short":"T"},
        "2":{  "long":"REAL_TIME_LIMIT_EXCEEDED","short":"T"},
        "3":{  "long":"MEMORY_LIMIT_EXCEEDED",   "short":"M"},
        "4":{  "long":"RUNTIME_ERROR",           "short":"R"},
        "5":{  "long":"SYSTEM_ERROR",            "short":"S"},
        "6":{  "long":"COMPILE_ERROR",           "short":"C"},
        "7":{  "long":"IDLENESS_LIMIT_EXCEEDED", "short":"I"},
        "8":{  "long":"SUM_TIME_LIMIT_EXCEEDED", "short":"T"}
}


# socket respone message ID
# MID 值
PREPARE_JUDGE   =0
START_JUDGE     =1
COMPILING       =2
JUDGING         =3
END_JUDGE       =4

# 默认的stack_limit

DEFAULT_STACK_LIMIT = 1024  # MB


