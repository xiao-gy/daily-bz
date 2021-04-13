import os

def download_aria2(headers,url,id):
    try:
        print(os.path.join(os.getcwd(),'bz',id))
        os.mkdir(os.path.join(os.getcwd(),'bz',id))
    except Exception:
        pass
    f = open(os.path.join(os.getcwd(),'bz',id,'file.txt'), mode='w+')
    for i in url:
        f.write(i+'\n')
    f.close()
    os.system('aria2c --conf-path=./config/aria.conf -d '+os.path.join(os.getcwd(),'bz',id)+' -i '+os.path.join(os.getcwd(),'bz',id,'file.txt'))

if __name__ == "__main__":
    headers= {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }
    download_aria2(headers,['https://i0.bspcdn.xyz/galleries/1886534/1.jpg'],'354876')
