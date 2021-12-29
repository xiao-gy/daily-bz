import os

from get import *
from download import download_aria2
from collection import *
from setting import *


url_list = search('blade')
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