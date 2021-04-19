import os

from main import main
from check import check
from get_list import get_bzlist
from get_detail import get_bzdetail
from get_imglink import get_imglink
from download_img import download_img
from download_aria2 import download_aria2
from zip import zip_file

#各项变量设置
url_base = 'https://zhb.eehentai.com'
headers= {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }

def home():
    global url_base
    global header
    opt=int(input('''=================欢迎使用Daily_bz=================
1) 爬取本子
2) 校验本子
3) 筛选本子
4) 上传本子
5) 下载指定本子
0) 更新Nyahentai网址
你的选择是: '''))
    if opt == 1:
        main(url_base)
    elif opt == 2:
        check()
    elif opt == 3:
        pass
    elif opt == 4:
        os.system('./cowtransfer-uploader --hash ./bz.zip')
    elif opt == 5:
        id = input('输入你要下载的本子id: ')
        link = get_imglink(headers,url_base+'/g/'+id+'/')
        download_aria2(headers,link,id)
        get_bzdetail(headers,url_base,'/g/'+id+'/')
    elif opt == 0:
        url_base = input('新网址: ')
    else:
        print('请重新输入')

home()