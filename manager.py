import os

from main import main
from check import check

#各项变量设置
url_base = 'https://zhb.eehentai.com'

def home():
    global url_base
    opt=int(input('''=================欢迎使用Daily_bz=================
1) 爬取本子
2) 校验本子
3) 筛选本子
4) 上传本子
5) 更新Nyahentai网址
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
        url_base = input('新网址: ')
    else:
        print('请重新输入')

home()