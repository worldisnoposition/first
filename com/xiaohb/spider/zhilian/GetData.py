from urllib import request # 请求url, 支持 HTTP(0.9/1.0) / FTP / 本地文件 / URL
'''from urllib import parse # 解析url, 支持 file / ftp / gopher / hdl / http / https / imap / mailto / mms / news / nntp / prospero / rsync / rtsp / rtspu / sftp / shttp / sip / sips / snews / svn / svn+ssh / telnet / wais
from urllib import robotparser # 分析 robots.txt 文件
from urllib import error # 异常'''
import requests
import urllib
import re # 正则模块
from bs4 import BeautifulSoup
import os
import inspect
def test(url):
    try:
        request = urllib.request.Request(url)
        requestdata = {}
        header = {'Host': 'sou.zhaopin.com',
                        'Connection': 'keep-alive',
                        'Pragma': 'no-cache',
                        'Cache-Control': 'no-cache',
                        'Upgrade-Insecure-Requests': '2',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                        'Referer': 'http://www.zhaopin.com/?utm_source=other&utm_medium=cnt&utm_term=&utm_campaign=121113803&utm_provider=zp&sid=121113803&site=pzzhubiaoti',
                        'Accept-Encoding': 'gzip, deflate',
                        'Accept-Language': 'zh-CN,zh;q=0.8',
                        'Cookie': 'urlfrom=121113803; urlfrom2=121113803; adfcid=pzzhubiaoti; adfcid2=pzzhubiaoti; adfbid=0; adfbid2=0; dywez=95841923.1518890626.1.1.dywecsr=other|dyweccn=121113803|dywecmd=cnt|dywectr=%E6%99%BA%E8%81%94; _jzqa=1.1824283735321587500.1518890626.1518890626.1518890626.1; _jzqc=1; _jzqy=1.1518890626.1518890626.1.jzqsr=baidu|jzqct=%E6%99%BA%E8%81%94.-; _jzqckmp=1; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1518890627; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1518890627; dywea=95841923.1956850112759053800.1518890626.1518890626.1518890626.2; dywec=95841923; dyweb=95841923.1.9.1518892599660; __utmd=1; __utma=269921210.1191661586.1518890626.1518890626.1518890626.2; __utmb=269921210.1.9.1518892599663; __utmc=269921210; __utmz=269921210.1518890626.1.1.utmcsr=other|utmccn=121113803|utmcmd=cnt|utmctr=%E6%99%BA%E8%81%94'}
        #response = urllib.request.urlopen(url=url,data=requestdata,headers=header,method="GET")
        response = requests.get(url, data=requestdata, headers=header)
        req = urllib.request.urlopen(request)
        resposedata = req.read().decode("utf-8")
        print(req.status)
        print(resposedata)
        #
        # print(data)
    except IOError:
        req = None
    if req:
        soup = BeautifulSoup(resposedata, "html.parser")
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

url = 'https://sou.zhaopin.com/?jl=530&sf=6001&st=8000&kw=java&kt=3'
test(url)