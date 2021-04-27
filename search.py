import requests
import urllib
import quote
from retrying import retry
from lxml import etree

url_list = []

@retry(stop_max_attempt_number=5)
def search(headers,url_base,keyword):
    global url_list
    r = requests.get(url_base+'/search/q_'+keyword,headers=headers)
    html = etree.HTML(r.text)
    page_sum = int(html.xpath('//*[@id="content"]/section/span[@class="last"]/a/@data-ci-pagination-page')[0])
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
    print(search(headers,'https://zhb.eehentai.com/','C97'))