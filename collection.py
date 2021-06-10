import os
import json

from get_detail import get_bzdetail
from download import download_aria2

like_list=[]
like_name=[]
like_mark=[]

def add_collection(id,name,mark):
    global like_list,like_name,like_mark
    read_collection()
    if not mark:
        mark = ' '
    if not like_list.count(id) :
        if input('是否置顶(y/n): ') == 'y':
            like_list.insert(0,id)
            like_name.insert(0,name)
            like_mark.insert(0,mark)
        else:
            like_list.append(id)
            like_name.append(name)
            like_mark.append(mark)
    else:
        print('id已存在')
    save_collection()

def put_collection():
    global like_list,like_name,like_mark
    read_collection()
    for i in range(len(like_list)):
        print(i+1,like_list[i],like_name[i],like_mark[i])
    input('按下回车继续...')
    return

def del_collection(no):
    no = int(no)
    global like_list,like_name,like_mark
    read_collection()
    if not len(like_list) < no:
        del like_list[no-1]
        del like_name[no-1]
        del like_mark[no-1]
    else:
        print('编号未存在')
    save_collection()

def mark_collection(no):
    no = int(no)
    global like_list,like_name,like_mark
    read_collection()
    if not len(like_list) < no:
        mark = input('输入注释: ')
        if not mark:
            mark = ' '
        like_mark[no-1] = mark
    else:
        print('id未存在')
    save_collection()

def save_collection():
    global like_list,like_name,like_mark
    f = open(os.path.join(os.getcwd(),'config','like.json'),mode='w+',encoding='utf8')
    data = {
        "like_list": like_list,
        "like_name": like_name,
        "like_mark": like_mark
    }
    f.write(json.dumps(data,ensure_ascii=False))
    f.close()

def read_collection():
    global like_list,like_name,like_mark
    try:
        f = open(os.path.join(os.getcwd(),'config','like.json'),mode='r',encoding='utf8')
        conf= json.loads(f.read())
        like_list = conf['like_list']
        like_name = conf['like_name']
        like_mark = conf['like_mark']
        f.close()
    except Exception:
        save_collection()

if __name__ == "__main__":
    read_collection()
    put_collection()