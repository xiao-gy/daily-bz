import os
import json
import shutil

from main import main
from check import check
from get import *
from download import download_aria2
from zip import zip_file
from collection import *
from setting import *

def collection(opt = ''):
    put_fold()
    opt = input('1) 进入收藏夹\n2) 新建收藏夹\n3) 删除收藏夹\n4) 修改收藏夹名\n5) 下载收藏夹\n6) 分享收藏夹\n7) 导入收藏夹\n0) 返回主页\n你的选择是: ')
    if opt == '1':
        no = int(input('输入要进入的收藏夹编号: '))
        put_collection(no)
        opt = input('1) 查看收藏\n2) 添加收藏\n3) 取消收藏\n4) 修改备注\n5) 下载收藏\n6) 分享收藏夹\n0) 返回上级\n你的选择是: ')
        if opt == '1':
            put_collection(no)
        elif opt == '2':
            id = input('输入id: ')
            name,tags,page = get_bzdetail(id)
            add_collection(no,id,name,input('输入注释: '))
        elif opt == '3':
            del_collection(no,input('输入编号: '))
        elif opt == '4':
            mark_collection(no,input('输入编号: '))
        elif opt == '5':
            download_collection(no)
        elif opt == '6':
            share_fold(no)
    elif opt == '2':
        name = input('输入要新建的收藏夹名: ')
        add_fold(name)
    elif opt == '3':
        no = int(input('输入要删除的收藏夹编号: '))
        del_fold(no)
    elif opt == '4':
        no = int(input('输入要修改名称的收藏夹编号: '))
        rename_fold(no)
    elif opt == '5':
        no = int(input('输入要下载内容的收藏夹编号: '))
        download_collection(no)
    elif opt == '6':
        no = int(input('输入要分享的收藏夹编号: '))
        share_fold(no)
    elif opt == '7':
        load_fold()
    elif opt == '0':
        return
    collection()

def repair(opt = ''):
    opt = input('1) 更新json文件\n2) 更新file.txt\n3) 补全全部本子\n你的选择是: ')
    if opt == '1':
        for i in list(os.walk(os.path.join(os.getcwd(),'bz')))[0][1]:
            get_bzdetail(i)
    elif opt == '2':
        for i in list(os.walk(os.path.join(os.getcwd(),'bz')))[0][1]:
            link = get_imglink(i)
            f = open(os.path.join(os.getcwd(),'bz',i,'file.txt'), mode='w+')
            for i in link:
                f.write(i+'\n')
            f.close()
    elif opt == '3':
        check()

def search():
    url_list = search(input('请输入关键词: '))
    for i in url_list:
        id = i[3:-1]
        print(id)
        try:
            os.mkdir(os.path.join(os.getcwd(),'bz',id))
        except Exception:
            pass
        link = get_imglink(id)
        get_bzdetail(id)
        download_aria2(link,id,1)

def screen():
    opt = input('1) 删除不包含指定tag的本子\n2) 删除包含指定tag的本子\n你的选择是: ')
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

def home(opt = ''):
    global info
    #各项变量设置
    version,headers,url_base,t_tag,nick = info()
    if opt == '':
        opt=input('''=================欢迎使用Daily_bz=================
1) 爬取本子
2) 下载指定本子
3) 筛选本子
4) 上传本子
5) 搜索本子
6) 文件补全
7) 我的收藏
9) 设置信息
0) 退出程序
你的选择是: ''')
    if opt == '1':
        main()
    elif opt == '2':
        id = input('输入你要下载的本子id: ')
        link = get_imglink(id)
        get_bzdetail(id)
        download_aria2(link,id,1)
    elif opt == '3':
        screen()
    elif opt == '4':
        zip_file('bz')
        os.system('./cowtransfer-uploader --hash ./bz.zip')
    elif opt == '5':
        search()
    elif opt == '6':
        repair()
    elif opt == '7':
        collection()
    elif opt == '9':
        setting()   
    elif opt == '0':
        exit()
    else:
        print('请重新输入')
    home()

try:
    os.mkdir(os.path.join(os.getcwd(),'bz'))
except Exception:
    pass

home()
