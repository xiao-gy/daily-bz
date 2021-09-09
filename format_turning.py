import json
import os

try:
    os.rename(os.path.join(os.getcwd(),'config','like.json'),os.path.join(os.getcwd(),'config','like_copy.json'))
except:
    print("无法进行重命名")

f = open(os.path.join(os.getcwd(),'config','like_copy.json'),mode='r',encoding='utf8')
likes = json.loads(f.read())

list={"likes":[]}

for i in range(0,len(likes['like_list'])):
    list['likes'].append({"id":likes['like_list'][i],"name":likes['like_name'][i],"mark":likes['like_mark'][i]})

f = open(os.path.join(os.getcwd(),'config','like.json'),mode='w+',encoding='utf8')
f.write(json.dumps(list,ensure_ascii=False))
f.close()