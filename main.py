import os

from get import *
from download import download_aria2
from zip import zip_file
from setting import info

version,headers,url_base,t_tag = info()

def main():
    try:
        os.mkdir(os.path.join(os.getcwd(),'bz'))
    except Exception:
        pass

    try:
        os.remove(os.path.join(os.getcwd(),'config','aria2.log'))
    except Exception:
        pass

    url_list = get_bzlist()
    for i in url_list:
        id = i[3:-1]
        print(id)
        try:
            os.mkdir(os.path.join(os.getcwd(),'bz',id))
        except Exception:
            pass
        link = get_imglink(id)
        try:
            get_bzdetail(id)
            download_aria2(link,id,0)
        except Exception:
            pass

if __name__ == "__main__":
    main()
    zip_file('bz')
