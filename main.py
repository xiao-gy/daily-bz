import os
from sys import executable

from get import *
from download import download_aria2
from zip import zip_file

headers= {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}
url_base = 'https://zhb.eehentai.com'

def main(url_base):
    try:
        os.mkdir(os.path.join(os.getcwd(),'bz'))
    except Exception:
        pass

    try:
        os.remove(os.path.join(os.getcwd(),'config','aria2.log'))
    except Exception:
        pass

    url_list = get_bzlist(headers,url_base)
    for i in url_list:
        id = i[3:-1]
        print(id)
        try:
            os.mkdir(os.path.join(os.getcwd(),'bz',id))
        except Exception:
            pass
        link = get_imglink(headers,url_base+i)
        try:
            get_bzdetail(headers,url_base,i)
            download_aria2(headers,link,id,0)
        except Exception:
            pass

if __name__ == "__main__":
    main(url_base)
    zip_file('bz')
