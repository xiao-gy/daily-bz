import os
import json

from get import get_bzdetail
from download import download_aria2
from get import *

list = {"likes":[{"name":"默认收藏夹","contents":[]}]}

def put_fold():
    global list
    read_collection()
    for i in range(len(list['likes'])):
        print(i+1,list['likes'][i]['name'],len(list['likes'][i]['contents']))
    return

def add_collection(no,id,name,mark):
    no = no-1
    global list
    read_collection()
    if not mark:
        mark = ' '
    for i in list['likes'][no]['contents']:
        if i['id'] == id:
            print("id已存在")
            return
    if input('是否置顶(y/n): ') == 'y':
        list['likes'][no]['contents'].insert(0,{"id":id,"name":name,"mark":mark})
    else:
        list['likes'][no]['contents'].append({"id":id,"name":name,"mark":mark})
    save_collection()

def put_collection(no=-1):
    global list
    read_collection()
    if no == -1:
        no  = int(input('输入要输出的收藏夹编号: '))
    no = no-1
    if len(list['likes'][no]['contents']) == 0:
        print('该收藏夹为空')
    else:
        for i in range(len(list['likes'][no]['contents'])):
            print(i+1,list['likes'][no]['contents'][i]['id'],list['likes'][no]['contents'][i]['name'],list['likes'][no]['contents'][i]['mark'])
    return

def del_collection(no,opt):
    no = no-1
    opt = int(opt)
    global list
    read_collection()
    if not len(list['likes'][no]['contents']) < opt:
        del list['likes'][no]['contents'][opt-1]
    else:
        print('编号未存在')
    save_collection()

def mark_collection(no,opt):
    no = no-1
    opt = int(opt)
    global list
    read_collection()
    if not len(list['likes'][no]['contents']) < opt:
        mark = input('输入注释: ')
        if not mark:
            mark = ' '
        list['likes'][no]['contents'][opt-1]['mark'] = mark
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

def download_collection(no):
    no = no-1
    read_collection()
    for i in list['likes'][no]['contents']:
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
    read_collection()
    add_collection(0,1,1,1)
    put_fold()
    put_collection(0)
    del_collection(0,1)
    #download_collection()