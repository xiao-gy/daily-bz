import os
import json

def download_form(id,mod):
    f = open(os.path.join(os.getcwd(),'bz',id,'file.txt'),'r')
    link = f.readlines()
    f.close()
    f = open(os.path.join(os.getcwd(),'bz',id,'temp.txt'), mode='w+')
    for k in link :
        name = k.split("/")[-1][:-1]
        if not os.path.exists(os.path.join(os.getcwd(),'bz',id,name)):
            if name.split(".")[1] == 'jpg':
                f.write(k[0:-5]+'.png'+'\n')
            else:
                f.write(k[0:-5]+'.jpg'+'\n')
    f.close()
    os.system('aria2c --conf-path=./config/aria2.conf -d '+os.path.join(os.getcwd(),'bz',id)+' -i '+os.path.join(os.getcwd(),'bz',id,'temp.txt'))
    os.remove(os.path.join(os.getcwd(),'bz',id,'temp.txt'))
    #重打标签
    if mod:
        f = open(os.path.join(os.getcwd(),'bz',id,'info.json'), mode='r',encoding="utf-8")
        data = dict(json.load(f))
        data['state'] = "checked"
        f.close()
        f = open(os.path.join(os.getcwd(),'bz',id,'info.json'), mode='w+',encoding="utf-8")
        f.write(json.dumps(data,ensure_ascii=False))

def download_aria2(url,id,mod):
    try:
        #print(os.path.join(os.getcwd(),'bz',id))
        os.mkdir(os.path.join(os.getcwd(),'bz',id))
    except Exception:
        pass
    f = open(os.path.join(os.getcwd(),'bz',id,'file.txt'), mode='w+')
    for i in url:
        f.write(i+'\n')
    f.close()
    #print('aria2c --conf-path=./config/aria2.conf -d '+os.path.join(os.getcwd(),'bz',id)+' -i '+os.path.join(os.getcwd(),'bz',id,'file.txt'))
    os.system('aria2c --conf-path=./config/aria2.conf -d '+os.path.join(os.getcwd(),'bz',id)+' -i '+os.path.join(os.getcwd(),'bz',id,'file.txt'))
    download_form(id,mod)

if __name__ == "__main__":
    headers= {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }
    download_aria2(headers,['https://i0.bspcdn.xyz/galleries/1886534/1.jpg'],'354876')