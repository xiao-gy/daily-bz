import os

def download_form(id):
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

if __name__ == "__main__":
    download_form('356008')
