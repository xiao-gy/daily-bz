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

def home(opt):
    global info
    #各项变量设置
    version,headers,url_base,t_tag = info()
    if opt == '':
        opt=input('''=================欢迎使用Daily_bz=================
1) 爬取本子
2) 下载指定本子
3) 筛选本子
4) 上传本子
5) 搜索本子
6) 信息完善
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
    elif opt == '4':
        zip_file('bz')
        os.system('./cowtransfer-uploader --hash ./bz.zip')
    elif opt == '5':
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
    elif opt == '6':
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
    elif opt == '7':
        opt = input('1) 查看收藏\n2) 添加收藏\n3) 取消收藏\n4) 修改备注\n5) 下载收藏\n0) 返回主页\n你的选择是: ')
        if opt == '1':
            put_collection()
        elif opt == '2':
            id = input('输入id: ')
            name,tags,page = get_bzdetail(id)
            add_collection(id,name,input('输入注释: '))
        elif opt == '3':
            put_collection()
            del_collection(input('输入编号: '))
        elif opt == '4':
            put_collection()
            mark_collection(input('输入编号: '))
        elif opt == '5':
            download_collection()
        elif opt == '0':
            home('')
        home('7')
    elif opt == '9':
        setting()   
    elif opt == '0':
        exit()
    else:
        print('请重新输入')
        home('')

    home('')

try:
    os.mkdir(os.path.join(os.getcwd(),'bz'))
except Exception:
    pass

home('')