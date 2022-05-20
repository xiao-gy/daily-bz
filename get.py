import requests
import json
import os
from retrying import retry
from lxml import etree
from setting import info

version,headers,url_base,t_tag,nick = info()

#proxies={"http": "socks5h://127.0.0.1:10808","https": "socks5h://127.0.0.1:10808"}

@retry(stop_max_attempt_number=5)
def get_bzlist(url):
    #r = requests.get(url,headers=headers,proxies=proxies,verify=False)
    r = requests.get(url,headers=headers)
    #print(r.text)
    html = etree.HTML(r.text)
    html_data = html.xpath('//a[@class="cover"]/@href')
    url_list=[]
    for i in html_data:
        url_list.append(i)
    return url_list

@retry(stop_max_attempt_number=5)
def get_imglink(id):
    url_add = '/g/'+id+'/'
    #r = requests.get(url_base+url_add,headers=headers,proxies=proxies,verify=False)
    r = requests.get(url_base+url_add,headers=headers)
    html = etree.HTML(r.text)
    html_data = html.xpath('//a[@class="gallerythumb"]/img[@class="lazyload"]/@data-src')
    page = len(html_data) #页数
    #r = requests.get(url_base+url_add+'1/',headers=headers,proxies=proxies,verify=False)
    r = requests.get(url_base+url_add+'1/',headers=headers)
    html = etree.HTML(r.text)
    html_data = html.xpath('//section[@id="image-container"]/a/img/@src')[0]
    format = html_data[-3:] #jpg or png
    url = []
    for i in range(0,page):
        url.append(html_data[:-5]+str(i+1)+'.'+format)
    return url

@retry(stop_max_attempt_number=5)
def get_bzdetail(id):
    url_add = '/g/'+id+'/'
    try:
        os.mkdir(os.path.join(os.getcwd(),'bz',id))
    except Exception:
        pass
    #r = requests.get(url_base+url_add,headers=headers,proxies=proxies,verify=False)
    r = requests.get(url_base+url_add,headers=headers)
    html = etree.HTML(r.text)
    #title
    name = ''
    for i in html.xpath('//*[@class="title"][last()]/span/text()'):
        name = name + i
    #tag
    tags = html.xpath('//section[@id="tags"]//span[@class="tags"]/a/span[@class="name"]/text()')[:-1]
    #page_sum
    page = int(html.xpath('//section[@id="tags"]//span[@class="tags"]/a/span[@class="name"]/text()')[-1])
    data = {
        "id": id,
        "name": name,
        "tags": tags,
        "page": page,
        "state": "unchecked"
    }
    f = open(os.path.join(os.getcwd(),'bz',id,'info.json'), mode='w+',encoding="utf-8")
    f.write(json.dumps(data,ensure_ascii=False))
    return name,tags,page

@retry(stop_max_attempt_number=5)
def get_search(keyword):
    global url_list
    url_list = []
    #r = requests.get(url_base+'/search/?q='+keyword,headers=headers,proxies=proxies,verify=False)
    r = requests.get(url_base+'/search/?q='+keyword,headers=headers)
    html = etree.HTML(r.text)
    try:
        page_sum = int(html.xpath('//a[@class="last"]/@href')[0].split("=")[-1])
    except Exception:
        page_sum = 1
    page = int(input('共 '+str(page_sum)+' 页,请输入你要下载的页数: '))
    for i in range(min(page,page_sum)):
        url_list = url_list+get_bzlist(url_base+'/search/?q='+keyword+'&page='+str(i+1))
    return url_list

if __name__ == "__main__":
    headers= {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }
    #print(get_bzlist(url_base))
    #print(get_imglink('397639'))
    get_bzdetail('397639')
    #print(search('c97'))
