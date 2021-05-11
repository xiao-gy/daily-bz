import os
import json
import shutil

from main import main
from check import check
from get_list import get_bzlist
from get_detail import get_bzdetail
from get_imglink import get_imglink
from download_img import download_img
from download_aria2 import download_aria2
from zip import zip_file
from screen import screen_tag
from search import search
from download_form import download_form
from collection import *
from setting import *

def home():
    global info
    #各项变量设置
    version,headers,url_base,t_tag = info()

    opt=input('''=================欢迎使用Daily_bz=================
1) 爬取本子
2) 校验本子
3) 筛选本子
4) 上传本子
5) 下载指定本子
6) 搜索本子
7) 信息完善
8) 我的收藏
0) 设置信息
你的选择是: ''')
    if opt == '1':
        main(url_base)
    elif opt == '2':
        check()
    elif opt == '3':
        opt = input('1) 筛选包含指定tag的本子\n2) 筛选除了指定tag之外的本子\n你的选择是: ')
        if opt == '1':
            bool = True
        elif opt == '2':
            bool = False
        for i in list(os.walk(os.path.join(os.getcwd(),'bz')))[0][1]:
            f = open(os.path.join(os.getcwd(),'bz',i,'info.json'),mode='r',encoding='utf8')
            info = json.loads(f.read())
            #print(json,screen_tag(json['tags'],t_tag,bool))
            #return
            f.close()
            if screen_tag(info['tags'],t_tag,bool) == False:
                shutil.rmtree(os.path.join(os.getcwd(),'bz',i))
    elif opt == '4':
        zip_file('bz')
        os.system('./cowtransfer-uploader --hash ./bz.zip')
    elif opt == '5':
        id = input('输入你要下载的本子id: ')
        link = get_imglink(headers,url_base+'/g/'+id+'/')
        download_aria2(headers,link,id)
        get_bzdetail(headers,url_base,'/g/'+id+'/')
        download_form(id)
    elif opt == '6':
        url_list = search(headers,url_base,input('请输入关键词: '))
        for i in url_list:
            id = i[3:-1]
            print(id)
            link = get_imglink(headers,url_base+i)
            download_aria2(headers,link,id)
            get_bzdetail(headers,url_base,i)
    elif opt == '7':
        opt = input('1) 更新json文件\n2) 更新file.txt\n3) 补全指定id本子图片\n你的选择是: ')
        if opt == '1':
            for i in list(os.walk(os.path.join(os.getcwd(),'bz')))[0][1]:
                url_add = '/g/'+i+'/'
                get_bzdetail(headers,url_base,url_add)
        elif opt == '2':
            for i in list(os.walk(os.path.join(os.getcwd(),'bz')))[0][1]:
                link = get_imglink(headers,url_base+'/g/'+i+'/')
                f = open(os.path.join(os.getcwd(),'bz',i,'file.txt'), mode='w+')
                for i in link:
                    f.write(i+'\n')
                f.close()
        elif opt == '3':
            id = input('输入要补全的本子id: ')
            os.system('aria2c --conf-path=./config/aria2.conf -d '+os.path.join(os.getcwd(),'bz',id)+' -i '+os.path.join(os.getcwd(),'bz',id,'file.txt'))
            download_form(id)
    elif opt == '8':
        opt = input('1) 查看收藏\n2) 添加收藏\n3) 取消收藏\n4) 修改备注\n你的选择是: ')
        if opt == '1':
            put_collection()
        elif opt == '2':
            id = input('输入id: ')
            name,tags,page = get_bzdetail(headers,url_base,'/g/'+id+'/')
            add_collection(id,name,input('输入注释: '))
        elif opt == '3':
            del_collection(input('输入id: '))
        elif opt == '4':
            mark_collection(input('输入id: '))
        home()
    elif opt == '0':
        setting()
        home()
    else:
        print('请重新输入')
        home()

try:
    os.mkdir(os.path.join(os.getcwd(),'bz'))
except Exception:
    pass

home()