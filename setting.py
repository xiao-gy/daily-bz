import os

#输入程序基本信息
version = 'v0.3'
url_base = 'https://zhb.eehentai.com'
headers= {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }
t_tag =[]

def read():
    pass

def save():
    pass

def info():
    json = {
        'version': version,
        'heasers': headers
        'url_base': url_base,
        't_tag': t_tag
    }
    return json

def setting():
    opt = input('1) 更新 Nyahentai 网址\n2) 输入 t_tag\n你的选择是: ')
    if opt == '1':
            url_base = input('新网址: ')
    elif opt == '2':
        t_tag = input('输入t_tag列表(请直接使用,分割): ').strip(',').split(',')