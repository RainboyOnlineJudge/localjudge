# 本地评测用

 - [安装]()
 - [如何使用]()
   - [评测单个代码]()
   - [评测多人多个代码--比赛模式]()
 - [其它技巧]()
   - [同时输出结果到屏幕和文件]()

## 一.安装

在`ubuntu 16.04 server`上安装如下

```
git clone https://github.com/RainboyOlineJudge/localjudge.git
sudo apt-get install python-pip3 libseccomp
sudo pip3 install pyyaml
cd localjudge
git submodule init && git submodule update
cd qjudge && sudo ./install.sh && cd ..
cd checker && sudo ./install.sh && cd ..
cd ujudge && sudo ./install.sh && cd ..
```

## 二.如何使用

### 2.1 评测单个代码

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

### 其它参数

 - score,`--score=100`,分值,默认100

### 2.2 评测多人多个代码--比赛模式


`config.yaml`样例如下

```yaml
name: 比赛名字
# 数据目录,含有 子目录,名为 aplusb1,等
data_base_path: demo/contest
# 选手所在的目录
user_base_path: demo/contest/user
problems:
 - name: aplusb1
   time: 1
   memory: 128
   core: 100   #default
   spj: fcmp2   #default
 - name: aplusb2
   time: 1
   memory: 512
   core: 200   #set by self
   # spj: spj.cpp
 - name: aplusb3
   time: 2
   memory: 64
   spj: fcmp2
```

命令行参数

```sh
sudo python lj.py --config=yaml_config_path
```

例如:
```sh
sudo python lj.py --config=config.yaml
```

注意:一旦你使用`--config`这个参数,就会进入比赛模式,其它参数就会失去作用.




## 如何同时输出到屏幕和文件?

```sh
sudo lj.py --config=1.yaml | & tee out
```

## 没有解决的问题:

 - [ ] 设定输出的文件夹,是否在测完后删除输出文件夹
 - [ ] 多语言评测:`python3 c++ c pascal`
 - [ ] stack限制
