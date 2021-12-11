import os
import json

from download import download_form
from get import get_bzdetail
from setting import info

version,headers,url_base,t_tag,nick = info()

def check():
    for i in list(os.walk(os.path.join(os.getcwd(),'bz')))[0][1]:
        try:
            f = open(os.path.join(os.getcwd(),'bz',i,'info.json'), mode='r',encoding="utf-8")
        except Exception:
            url_add = '/g/'+i+'/'
            get_bzdetail(url_add)
            f = open(os.path.join(os.getcwd(),'bz',i,'info.json'), mode='r',encoding="utf-8")
        data = dict(json.load(f))
        if not data['state'] == 'checked':
            os.system('aria2c --conf-path=./config/aria2.conf -d '+os.path.join(os.getcwd(),'bz',i)+' -i '+os.path.join(os.getcwd(),'bz',i,'file.txt'))
            download_form(i,1)

if __name__ == "__main__":
    check()