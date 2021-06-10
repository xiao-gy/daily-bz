import requests
import json
import os
from retrying import retry
from lxml import etree

@retry(stop_max_attempt_number=5)
def get_bzlist(headers,url_base):
    r = requests.get(url_base,headers=headers)
    html = etree.HTML(r.text)
    html_data = html.xpath('//*[@id="content"]/div/div/a/@href')
    url_list=[]
    for i in html_data:
        url_list.append(i)
    return url_list


@retry(stop_max_attempt_number=5)
def get_imglink(headers,url):
    r = requests.get(url+'list2/',headers=headers)
    html = etree.HTML(r.text)
    html_data = html.xpath('//*[@id="image-container"]/img[@class="list-img lazyload"]/@data-src')
    return html_data

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
        "page": page,
        "state": "unchecked"
    }
    f = open(os.path.join(os.getcwd(),'bz',url_add[3:-1],'info.json'), mode='w+',encoding="utf-8")
    f.write(json.dumps(data,ensure_ascii=False))
    return name,tags,page

@retry(stop_max_attempt_number=5)
def search(headers,url_base,keyword):
    global url_list
    url_list = []
    r = requests.get(url_base+'/search/q_'+keyword,headers=headers)
    html = etree.HTML(r.text)
    try:
        page_sum = int(html.xpath('//*[@id="content"]/section/span[@class="last"]/a/@data-ci-pagination-page')[0])
    except Exception:
        page_sum = 1
    page = int(input('共 '+str(page_sum)+' 页,请输入你要下载的页数: '))
    for i in range(min(page,page_sum)):
        r = requests.get(url_base+'/search/q_'+keyword+'/page/'+str(i+1),headers=headers)
        html = etree.HTML(r.text)
        html_data = html.xpath('//*[@id="content"]/div/div/a/@href')
        for i in html_data:
            url_list.append(i)
    return url_list

if __name__ == "__main__":
    headers= {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }
    print(get_imglink(headers,'https://zhb.eehentai.com/g/354876/'))
    get_bzdetail(headers,'https://zhb.eehentai.com','/g/354876/')
    print(search(headers,'https://zhb.eehentai.com/','泳装'))
