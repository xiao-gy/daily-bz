import urllib
import requests
requests.packages.urllib3.disable_warnings()
# CK = 'e5fe7daab1b64929981cd4ddc38d232c'
CK = 'e0d55ea7d2f640eb816f8058540a11ba'
# param = 'answers=["0","0","0","2","0","1","1","0"]&\
# llatitude=30.826655&\
# longitude=104.185025&\
# country=中国&\
# city=成都市&\
# district=新都区&\
# province=四川省&\
# township=新都大道&\
# street=新都大道八号&\
# areacode=510114'
# param = 'answers=["0","0","0","2","0","1","1","0"]&\
para = {
	'answers': '["0","0","0","0","2","0","1","1","0","1"]',
	'latitude': '30.82404',
	'longitude': '104.15801',
	'country': '中国',
	'city': '成都市',
	'district': '新都区',
	'province': '四川省',
	'township': '新都大道',
	'street': '新都大道八号',
	'areacode': '510114'
}
src = urllib.parse.urlencode(para)
# print(src)
# exit()
# param = 'answers=["0","0","0","0","2","0","1","1","0","1"]&\
# 	latitude=30.65&\
# 	longitude=104.05&\
# 	country=%E4%B8%AD%E5%9B%BD&\
# 	city=%E6%88%90%E9%83%BD%E5%B8%82&\
# 	district=%E6%AD%A6%E4%BE%AF%E5%8C%BA&\
# 	province=%E5%9B%9B%E5%B7%9D%E7%9C%81&\
# 	township=%E6%96%B0%E9%83%BD%E5%A4%A7%E9%81%93&\
# 	street=%E6%96%B0%E9%83%BD%E5%A4%A7%E9%81%93%E5%85%AB%E5%8F%B7&\
# 	areacode=510107'
UA = 'Mozilla/5.0 (iPhone;CPU iPhone OS15_0_1 like Mac OS X)AppleWebKit/605.1.15(KHTML,like Gecko)Mobile/15E148MicroMessenger/8.0.10(0x18000a2a)NetType/WIFILanguage/zh_CN'
url = 'https://student.wozaixiaoyuan.com/health/save.json'
pushtype = 'application/x-www-form-urlencoded;charset=UTF-8'
header = {'UserAgent': UA, 'JWSESSION': CK, 'Content-Type': pushtype}
res = requests.post(url, data=src, headers=header, verify=False)
code = res.status_code
if code == '200':
    print('RESULT:', res.text)
    print('STATUS:', res.status_code)
else:
    print('RESULT:', res.text)
    print('STATUS:', res.status_code)
