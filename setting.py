import os
import json

#输入程序基本信息
version = 'v0.3'
url_base = 'https://zhb.eehentai.com'
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }
t_tag =[]

def read():
    f = open(os.path.join(os.getcwd(),'config','config.json'),mode='r',encoding='utf8')
    conf= json.loads(f.read())
    version = conf['version']
    url_base = conf['url_base']
    headers = conf['headers']
    t_tag = conf['t_tag']
    f.close()

def save():
    f = open(os.path.join(os.getcwd(),'config','config.json'),mode='w+',encoding='utf8')
    data = {
        "version": version,
        "url_base": url_base,
        "headers": headers,
        "t_tag": t_tag
    }
    f.write(json.dumps(data,ensure_ascii=False))
    f.close()

def info():
    try:
        read()
    except Exception:
        pass
    return version,headers,url_base,t_tag

def setting():
    global url_base,t_tag
    opt = input('1) 更新 Nyahentai 网址\n2) 输入 t_tag\n你的选择是: ')
    if opt == '1':
        url_base = input('新网址: ')
    elif opt == '2':
        t_tag = input('输入t_tag列表(请直接使用,分割): ').strip(',').split(',')
    save()

if __name__ == "__main__":
    try:
        read()
    except Exception:
        save()