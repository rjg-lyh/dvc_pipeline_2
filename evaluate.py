import os
import sys
import yaml
import numpy as np
import random
import json

input = sys.argv[1]
params = yaml.safe_load(open("params.yaml"))["evaluate"]
number = params["number"]
random.seed(params['seed'])

path_in = os.path.join('data',input) #输入model路径

with open(path_in, 'r') as f:
    model = f.readline()             #读取model
    model = json.loads(model) 

new = random.sample(model, number)
result = sum(new)/sum(model)
#print("Result: ",result)

path_out = os.path.join('data','Result')
with open(path_out, 'w') as f:
    f.write(str(result))
print("pipeline is all done successfully")
