# 本地评测用

## 安装


```
sudo apt-get install python-pip3 libseccomp
sudo pip3 install pyyaml
cd qjudge && sudo ./install.sh
cd checker && sudo ./install.sh
cd ujudge && sudo ./install.sh
```

## 使用

评测一个题目


```
lj --src=main.cpp  --data=path_of_data
```

```
lj --src=main.cpp  --data=path_of_data --memroy=128 --time=1000 -output_path
```

```
lj --config_path=
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
