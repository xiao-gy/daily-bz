import os
import random
import json
from flask import Flask
from flask import render_template
from get import *
from download import *
from collection import *
from setting import *

app = Flask(__name__,template_folder='./static/templates')

all_bz = []

def random_bz(sum):
    global all_bz
    return random.sample(all_bz,min(sum,len(all_bz)))

def load_bzinfo():
    global all_bz
    if not all_bz:
        all_bz = []
    for i in os.listdir(os.path.join(os.getcwd(),'bz')):
        print(i)
        if os.path.exists(os.path.join(os.getcwd(),'bz',i,'info.json')):
            try:
                f = open(os.path.join(os.getcwd(),'bz',i,'info.json'),mode='r',encoding='utf8')
                bzinfo = json.loads(f.read())
                all_bz.append({"id":i,"name":bzinfo['name']})
            except Exception:
                pass

def get_bzinfo(id):
    try:
        f = open(os.path.join(os.getcwd(),'bz',id,'info.json'),mode='r',encoding='utf8')
        bzinfo = json.loads(f.read())
        name = bzinfo['name']
        tags = bzinfo['tags']
        page = int(bzinfo['page'])
    except Exception:
        name = ''
        tags = ''
        page = 0
    return {"id":id,"name":name,"tags":tags,"page":page}

@app.route("/")
def homepage():
    return render_template('home.html',recommend=all_bz[-1:-20:-1])

@app.route("/random/")
def randompage():
    return render_template('random.html',recommend=random_bz(20))

@app.route("/g/<id>/")
def datail(id):
    return render_template('detail.html',info=get_bzinfo(id),recommend=random_bz(20))

@app.route("/g/<id>/<number>/")
def img_detail(id,number):
    return render_template('image.html',id=id,number=int(number),all=get_bzinfo(id)['page'],next=str(int(number)+1))

@app.route("/img/<id>/<filename>.jpg")
def img(id,filename):
    with open(os.path.join(os.getcwd(),'bz',id,filename+'.jpg'),'rb') as f:
        image=f.read()
    f.close()
    return image

if __name__ == "__main__":
    load_bzinfo()
    app.run(
        host='0.0.0.0',
        port=5000
        )