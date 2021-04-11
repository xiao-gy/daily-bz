import requests
import urllib
import quote
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

if __name__ == "__main__":
    headers= {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }
    get_bzlist(headers,'https://zhb.eehentai.com/')