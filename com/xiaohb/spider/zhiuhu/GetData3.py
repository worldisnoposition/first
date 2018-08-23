from urllib import request
import re
from bs4 import BeautifulSoup
import requests
def getRequest(url):
    return request.urlopen(url)

def getXSRF(url):
    _xsrf = getRequest(url).headers._headers[9][1][6:38]
    soup = BeautifulSoup(getRequest(url).read().decode("utf-8"), "html.parser")
    input = soup.findAll(name='input', attrs={"type": 'hidden'})
    print(input[0]['value'])
    return input[0]['value']
    #return '36353337326263342d333061662d346530662d386435612d646265383366376332313664'

def login(baseurl,email,password):
    login_data = {
        '_xsrf': getXSRF(baseurl),
        'password': password,
        'remember_me': 'true',
        'email': email,
    }
    headers_base = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webq,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
        'Connection': 'keep-alive',
        'Host': 'http://www.zhihu.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel MacOS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',
        'Referer': 'http://www.zhihu.com/',
    }
    session = requests.session()
    baseurl += "/login/email"
    content = session.post(baseurl, headers=headers_base, data=login_data)
    print(content.text)
    s = session.get("http://www.zhihu.com", verify=False)
    print(s.text.encode('utf-8'))

url = "http://www.zhihu.com"
login(url,"1130183567@qq.com","zhihu_laji")