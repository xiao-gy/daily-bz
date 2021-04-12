import os
import shutil
import zipfile

def zip_file(src_dir):
    zip_name = src_dir.split("/")[-1]+'.zip'
    print(zip_name)
    z = zipfile.ZipFile(zip_name,'w',zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(src_dir):
        fpath = dirpath.replace(src_dir,'')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            z.write(os.path.join(dirpath, filename),fpath+filename)
            print ('==压缩成功==')
    z.close()

if __name__ == "__main__":
    zip_file('bz')
