import os
import json

#输入程序基本信息
version = 'v2.0 for nhentai with Web Gui'
url_base = 'https://nyahentai.red'
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }
t_tag =[]
nick = 'hentai'

def read():
    try:
        f = open(os.path.join(os.getcwd(),'config','config.json'),mode='r',encoding='utf8')
        conf= json.loads(f.read())
        version = conf['version']
        url_base = conf['url_base']
        headers = conf['headers']
        t_tag = conf['t_tag']
        nick = conf['nick']
        f.close()
    except Exception:
        save()

def save():
    f = open(os.path.join(os.getcwd(),'config','config.json'),mode='w+',encoding='utf8')
    data = {
        "version": version,
        "url_base": url_base,
        "headers": headers,
        "t_tag": t_tag,
        "nick": nick
    }
    f.write(json.dumps(data,ensure_ascii=False))
    f.close()

def info():
    try:
        read()
    except Exception:
        pass
    return version,headers,url_base,t_tag,nick

def setting():
    global url_base,t_tag,nick
    opt = input('1) 更新 Nyahentai 网址\n2) 输入 t_tag\n3) 修改昵称\n你的选择是: ')
    if opt == '1':
        url_base = input('新网址: ')
    elif opt == '2':
        t_tag = input('输入筛选tag列表(请直接使用,分割): ').strip(',').split(',')
    elif opt == '3':
        nick = input('输入你要修改的昵称: ')
    save()

if __name__ == "__main__":
    try:
        read()
    except Exception:
        save()