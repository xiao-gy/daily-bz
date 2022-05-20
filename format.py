import os
from PIL import Image

dir = os.listdir(os.path.join(os.getcwd(),'bz'))
count=0
for i in dir:
    image = os.listdir(os.path.join(os.getcwd(),'bz',i))
    for k in image:
        name=k.split(".")
        if name[-1] == "png":
            img=Image.open(os.path.join(os.getcwd(),'bz',i,k))
            img = img.convert('RGB')
            name[-1] = "jpg"
            name = str.join(".", name)
            img.save(os.path.join(os.getcwd(),'bz',i,name))
            img.close()
            os.remove(os.path.join(os.getcwd(),'bz',i,k))
