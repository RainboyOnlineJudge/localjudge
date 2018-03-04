# 本地评测用

## 安装

有ubuntu 16.04 server上安装如下

```
git clone https://github.com/RainboyOlineJudge/localjudge
sudo apt-get install python-pip3 libseccomp
sudo pip3 install pyyaml
cd localjudge
git submodule init && git submodule update
cd qjudge && sudo ./install.sh
cd checker && sudo ./install.sh
cd ujudge && sudo ./install.sh
```

## 使用

评测一个题目

0.直接使用
会在当前目录下找`main.cpp`和`data/`数据文件目录,如果都找到就开始进行评测

```
lj
```


1.指明测试的源代码  和 `数据路径`
```
lj --src=main.cpp  --data=path_of_data
```

2.指明测试的源代码  和 `数据路径` ,内存大小(mb),时间(ms),输出路径
```
lj --src=main.cpp  --data=path_of_data --memroy=128 --time=1000 -output_path
```

3.通过配置文件来进行测试,可以进行比赛模式测试
```
lj --config=
```


比赛模式 评测多个人的比赛


yaml
```
name: 比赛名字1
data_base_path: /a/b/c
output_path: /a/b/c 输出文件的地址
problems:
 - name: aplusb1
   time: 1
   memory: 128
   spj: fcmp2   #default
 - name: aplusb2
   time: 1
   memory: 512
   spj: spj.cpp
 - name: aplusb3
   time: 2
   memory: 64
   spj: fcmp2
```

测试的过程:



## 没有解决的问题:

 - [ ] 设定输出的文件夹,是否在测完后删除输出文件夹
