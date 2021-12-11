import os
import json
from random import expovariate

from get import get_bzdetail
from download import download_aria2
from get import *

list = {"likes":[{"name":"默认收藏夹","contents":[]}],"others":[]}

def put_fold():
    global list
    read_collection()
    print('===========收藏夹===========')
    print('自有收藏夹:')
    if len(list['likes']) == 0 :
        print('无收藏夹')
    for i in range(len(list['likes'])):
        print(i+1,list['likes'][i]['name'],len(list['likes'][i]['contents']))
    print('其他收藏夹(来自分享\推荐):')
    if len(list['others']) == 0 :
        print('无收藏夹')
    for i in range(len(list['others'])):
        print(i+len(list['likes'])+1,list['others'][i]['name'],len(list['others'][i]['contents']))
    print()
    return

def add_fold(name):
    read_collection()
    list['likes'].append({"name":name,"contents":[]})
    save_collection()

def del_fold(no):
    read_collection()
    if no > len(list['likes']):
        sort = 'others'
        no = no - len(list['likes'])
    else:
        sort = 'likes'
    no = no - 1
    if input('是否删除收藏夹 '+list[sort][no]['name']+' (y/n): ') == 'y':
        del list[sort][no]
        save_collection()
    else:
        print('取消删除 '+list[sort][no]['name'])

def rename_fold(no):
    read_collection()
    if no > len(list['likes']):
        print('你只能修改自己的收藏夹!')
        return
    no = no - 1
    name = input('输入你要将 '+list['likes'][no]['name']+' 修改的名字: ')
    list['likes'][no-1]['name'] = name
    save_collection()

def share_fold(no):
    version,headers,url_base,t_tag,nick = info()
    if no > len(list['likes']):
        sort = 'others'
        no = no - len(list['likes'])
    else:
        sort = 'likes'
    no = no - 1
    read_collection()
    f = open(os.path.join(os.getcwd(),'share.json'),mode='w+',encoding='utf8')
    share = {"shared":[list[sort][no]]}
    share['shared'][0]['name'] = share['shared'][0]['name'] + '#' + nick
    f.write(json.dumps(share,ensure_ascii=False))
    f.close()
    print('文件生成 '+os.path.join(os.getcwd(),'share.json'))

def load_fold():
    read_collection()
    print('从 '+os.path.join(os.getcwd(),'share.json')+' 导入')
    try:
        f = open(os.path.join(os.getcwd(),'share.json'),mode='r',encoding='utf8')
        share = json.loads(f.read())
        list['others'] = list['others'] + share['shared']
        f.close()
    except Exception:
        print('导入错误')
    save_collection()

def add_collection(no,id,name,mark):
    global list
    read_collection()
    if no > len(list['likes']):
        print('你只能修改自己的收藏夹!')
        return
    no = no-1
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
    if no > len(list['likes']):
        sort = 'others'
        no = no - len(list['likes'])
    else:
        sort = 'likes'
    no = no - 1
    if len(list[sort][no]['contents']) == 0:
        print('该收藏夹为空')
    else:
        for i in range(len(list[sort][no]['contents'])):
            print(i+1,list[sort][no]['contents'][i]['id'],list[sort][no]['contents'][i]['name'],list[sort][no]['contents'][i]['mark'])
    return

def del_collection(no,opt):
    global list
    read_collection()
    if no > len(list['likes']):
        print('你只能修改自己的收藏夹!')
        return
    no = no-1
    if no > len(list['likes']):
        sort = 'others'
        no = no - len(list['likes'])
    else:
        sort = 'likes'
    opt = int(opt)
    if not len(list[sort][no]['contents']) < opt:
        del list[sort][no]['contents'][opt-1]
    else:
        print('编号未存在')
    save_collection()

def mark_collection(no,opt):
    read_collection()
    global list
    if no > len(list['likes']):
        print('你只能修改自己的收藏夹!')
        return
    no = no-1
    opt = int(opt)
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
    read_collection()
    if no > len(list['likes']):
        sort = 'others'
        no = no - len(list['likes'])
    else:
        sort = 'likes'
    no = no-1
    for i in list[sort][no]['contents']:
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
    del_collection(1,1)
    #download_collection('likes',1)