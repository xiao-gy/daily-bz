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

#各项变量设置
url_base = 'https://zhb.eehentai.com'
headers= {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }
t_tag =[]

def home():
    global url_base
    global headers
    global t_tag
    opt=input('''=================欢迎使用Daily_bz=================
1) 爬取本子
2) 校验本子
3) 筛选本子
4) 上传本子
5) 下载指定本子
6) 信息完善
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
    elif opt == '6':
        opt = input('1) 更新json文件\n2) 更新file.txt\n你的选择是: ')
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
    elif opt == '0':
        opt = input('1) 更新 Nyahentai 网址\n2) 输入 t_tag\n你的选择是: ')
        if opt == '1':
            url_base = input('新网址: ')
        elif opt == '2':
            t_tag = input('输入t_tag列表(请直接使用,分割): ').strip(',').split(',')
        home()
    else:
        print('请重新输入')
        home()

home()