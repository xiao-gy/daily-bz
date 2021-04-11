import requests
import urllib
import quote
from retrying import retry
from lxml import etree

@retry(stop_max_attempt_number=5)
def get_bzdetail(headers,url_base,url_add):
    r = requests.get(url_base+url_add,headers=headers)
    html = etree.HTML(r.text)
    html_data = html.xpath('//*[@id="cover"]/a/img/@alt')
    return html_data[0]

if __name__ == "__main__":
    headers= {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }
    print(get_bzdetail(headers,'https://zhb.eehentai.com','/g/354876/'))
