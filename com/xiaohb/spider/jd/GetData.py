from urllib import request # 请求url, 支持 HTTP(0.9/1.0) / FTP / 本地文件 / URL
from urllib import parse # 解析url, 支持 file / ftp / gopher / hdl / http / https / imap / mailto / mms / news / nntp / prospero / rsync / rtsp / rtspu / sftp / shttp / sip / sips / snews / svn / svn+ssh / telnet / wais
from urllib import robotparser # 分析 robots.txt 文件
from urllib import error # 异常
import re # 正则模块
from bs4 import BeautifulSoup
import os
import inspect
def test(url):
    try:
        req = request.urlopen(url)
        data = req.read().decode("utf-8")
        print(req.status)
        print(data)
        #
        # print(data)
    except IOError:
        req = None
    if req:
        soup = BeautifulSoup(data, "html.parser")
        a = soup.findAll(name='a', attrs={"href": re.compile(r'^http:')})
        print(a)
        for i in a:
            print(i)
        # req_attr = dir(req)
        # print(req_attr)
        # req_attr.reverse()
        # print(req_attr)
        # print(req_attr[::-1])
    #if(data):
     #   print(data)
test('http://www.jd.com')