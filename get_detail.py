import requests
import urllib
import quote
from retrying import retry
from lxml import etree
import json
import os

@retry(stop_max_attempt_number=5)
def get_bzdetail(headers,url_base,url_add):
    r = requests.get(url_base+url_add,headers=headers)
    html = etree.HTML(r.text)
    name = html.xpath('//*[@id="info"]/h1/text()')[0]
    tags = html.xpath('//span[@class="tags"]/a/text()')
    page = int(str(html.xpath('//*[@id="info"]/div[1]/text()'))[4:-4])
    for i in range(len(tags)):
        tags[i] = tags[i][:-1]
    data = {
        "id": url_add[3:-1],
        "name": name,
        "tags": tags,
        "page": page
    }
    f = open(os.path.join(os.getcwd(),'bz',url_add[3:-1],'info.json'), mode='w+',encoding="utf-8")
    f.write(json.dumps(data,ensure_ascii=False))

if __name__ == "__main__":
    headers= {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }
    get_bzdetail(headers,'https://zhb.eehentai.com','/g/354876/')
