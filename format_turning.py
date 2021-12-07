import json
import os

try:
    os.rename(os.path.join(os.getcwd(),'config','like.json'),os.path.join(os.getcwd(),'config','like_copy.json'))
except:
    print("无法进行重命名")

f = open(os.path.join(os.getcwd(),'config','like_copy.json'),mode='r',encoding='utf8')
likes = json.loads(f.read())

list = {"likes":[{"name":"默认收藏夹","contents":[]}]}

for i in likes['likes']:
    list['likes'][0]['contents'].append({"id":i['id'],"name":i['name'],"mark":i['mark']})

f = open(os.path.join(os.getcwd(),'config','like.json'),mode='w+',encoding='utf8')
f.write(json.dumps(list,ensure_ascii=False))
f.close()