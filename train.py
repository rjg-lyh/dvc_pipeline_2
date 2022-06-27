import os
import sys
import yaml
import numpy as np

input = sys.argv[1]
params = yaml.safe_load(open("params.yaml"))["train"]
epoch = params["epoch"]

path_in = os.path.join('data',input) #输入prepared路径

with open(path_in, 'r') as f:
    info = ''.join(f.readlines()) #读取prepared
result = info.split('\n')[:-1]
result = [int(x) for x in result]
for _ in range(epoch):      #给每个数据加epoch个1
    for i in range(len(result)):
        result[i] += 1
print(result)

result = np.array(result)
result = (result - result.mean())/result.std()  #数据归一化处理
print(result)
result = result.tolist()
print(result)
path_out = os.path.join('data','model')
with open(path_out, 'w') as f:  #将model存入data文件夹下
    f.write(str(result))

print("train stage finished")


