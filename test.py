# coding:utf-8

import yaml
import codecs
import os


yaml_path  = "1.yaml"

if not os.path.exists(yaml_path):
    print("没有打到配置文件")
    exit(1)

content = ''
with open(yaml_path) as f:
    content = f.read()

print(content)

config= yaml.load(content)

print(config)

# 设计思路

handler 处理一个题目
