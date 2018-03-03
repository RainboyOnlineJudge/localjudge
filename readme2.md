# 详细的流程:

# handler class 初始化

data:

 - `judger`:选择使用哪个评测机,这两个值这一: qjudge,ujudge,默认qjudge
 - `cmp`: 文件比较器,详细看`localjudge/checker`文件夹,也可以传入一个自定义的`spj.cpp`,详见下面
 - `output_size`:默认1024mb,文件输出的大小
 - `code`:代码
 - `time`:时间 s
 - `memory`:内存限制 mb
 - `lang`:cpp,c,pas,py

data_dir: 数据文件路径
output_dir: 数据输出路径

# handler 查检 data_dir 里的data是否存在

## 编译 compile

成功

代码失败

spj.cpp 编译失败

## 如果使用自定义的spj?

### 单测模式

```
--spj='/1/2/3/spj.cpp'
```

```
--spj=fcmp2
```

### 比赛模式

```yaml
 - spj:/1/2/3/spj.cpp
```
