import os
import sys
import yaml
import random

params = yaml.safe_load(open("params.yaml"))["prepare"]
number = params["number"]
random.seed(params["seed"])
input = sys.argv[1]
path_in = os.path.join('data',input) #输入的数据集路径

with open(path_in, 'r') as f:
    info = ''.join(f.readlines()) #读取数据集
result = info.split('\n')[:-1] #从数据集中读取出1~50
prepared = random.sample(result, number) # 随即抽取出number个数

path_out = os.path.join('data','prepared')
f = open(path_out, 'w')        #存入prepared数据
for ss in prepared:
    f.write(ss + '\n')
f.close()
print("prepare stage finished")
