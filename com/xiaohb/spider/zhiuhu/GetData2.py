#coding=utf-8
import requests
import re
#这种尝试彻底失败，卡在了第一步获取getContext返回500
#使用requests.get获取知乎首页的内容
def getContent(url):
    print url
    r = requests.get('http://www.zhihu.com')
    print r
    #requests.get().content是爬去网页的全部内容
    return r.content
#获取_xsrfhi标签的值
def getXSRF(url):
    ''''''
    #获取知乎首页内容
    content = getContent(url)
    print content
    #正则表达式的匹配模式
    pattern = re.compile('.*?<input type="hidden" name="_xsrf" value="(.*?)"/>.*?')
    #re.findall查找所有匹配的字符串
    match = re.findall(pattern, content)
    print match
    xsrf = match[0]
    #返回_xsrf的值
    return xsrf
#登录主方法
def login(baseurl,email,password):
    ''''''
    #post需要的表单数据，类型为字典
    login_data = {
        '_xsrf': getXSRF(baseurl),
        'password': password,
        'remember_me': 'true',
        'email': email,
    }
    #设置头信息
    headers_base = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webq,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
        'Connection': 'keep-alive',
        'Host': 'www.zhihu.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel MacOS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',
        'Referer': 'http://www.zhihu.com/',
    }
    #使用session登录，这样的好处是可以在接下来的访问中可以保留登录信息
    session = requests.session();
    #登录的URL
    baseurl += "/login/email"
    #requests的session登录，以post方式，参数分别为url、headers、data
    content = session.post(baseurl, headers = headers_base, data = login_data)
    #登录成功后输出{"r":0,"msg":"\u767b\u9646\u6210\u529f"}
    print content.text
    #再次使用session以get去访问知乎首页，一定要设置verify = False,否则会访问失败
    s = session.get("http://www.zhihu.com", verify = False)
    print s.text.encode('utf-8')
    #把爬下来的知乎首页写到文本中
    f = open('zhihu.txt', 'w')
    f.write(s.text.encode('utf-8'))

url = "http://www.zhihu.com/"
#进行登录，将星号替换成你的知乎登录邮箱和密码即可
login(url,"qqq@qqcom","asdf")