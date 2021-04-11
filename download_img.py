import requests
import os
from retrying import retry

@retry()
def download_img(headers,url,id):
    try:
        os.mkdir(os.path.join(os.getcwd(),'bz',id))
    except Exception:
        pass
    for i in url:
        imgname = i.split("/")[-1]
        imgpath = os.path.join(os.getcwd(),'bz',id,imgname)

        img_data = requests.get(i, allow_redirects=True).content
        with open(imgpath, 'wb') as handler:
            handler.write(img_data)

if __name__ == "__main__":
    headers= {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }
    download_img(headers,['https://i0.bspcdn.xyz/galleries/1886534/1.jpg'],'354876')
