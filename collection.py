import os
import json

from get import get_bzdetail
from download import download_aria2
from get import *

list = {"likes":[]}

def add_collection(id,name,mark):
    global list
    read_collection()
    if not mark:
        mark = ' '
    for i in list['likes']:
        if i['id'] == id:
            print("id已存在")
            return
    if input('是否置顶(y/n): ') == 'y':
        list['likes'].insert(0,{"id":id,"name":name,"mark":mark})
    else:
        list['likes'].append({"id":id,"name":name,"mark":mark})
    save_collection()

def put_collection():
    global list
    read_collection()
    for i in range(len(list['likes'])):
        print(i+1,list['likes'][i]['id'],list['likes'][i]['name'],list['likes'][i]['mark'])
    return

def del_collection(no):
    no = int(no)
    global list
    read_collection()
    if not len(list['likes']) < no:
        del list['likes'][no]
    else:
        print('编号未存在')
    save_collection()

def mark_collection(no):
    no = int(no)
    global list
    read_collection()
    if not len(list['likes']) < no:
        mark = input('输入注释: ')
        if not mark:
            mark = ' '
        list['likes'][no-1]['mark'] = mark
    else:
        print('id未存在')
    save_collection()

def save_collection():
    global list
    f = open(os.path.join(os.getcwd(),'config','like.json'),mode='w+',encoding='utf8')
    f.write(json.dumps(list,ensure_ascii=False))
    f.close()

def read_collection():
    global list
    try:
        f = open(os.path.join(os.getcwd(),'config','like.json'),mode='r',encoding='utf8')
        list = json.loads(f.read())
        f.close()
    except Exception:
        save_collection()

def download_collection():
    for i in list['likes']:
        try:
            os.mkdir(os.path.join(os.getcwd(),'bz',i['id']))
        except Exception:
            pass
        link = get_imglink(i['id'])
        try:
            get_bzdetail(i['id'])
            download_aria2(link,i['id'],1)
        except Exception:
            pass

def screen_tag(tag,t_tag,bool):
    if bool == True:
        return set(t_tag) <= set(tag)
    else:
        for i in t_tag:
            if i in tag:
                return False
        return True

if __name__ == "__main__":
    #add_collection(1,1,1)
    read_collection()
    put_collection()
    download_collection()