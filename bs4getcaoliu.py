## --*-- coding:utf-8 --*--
from bs4 import BeautifulSoup
import urllib2
import urllib
import requests
import re
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import socket
socket.setdefaulttimeout(120)


num=0
def ZhiZhuDownImag(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    #headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    req=urllib2.Request(url,headers=headers) #创建请求对象
    html=urllib2.urlopen(req,timeout=60)     #发送http请求
    htmlcontent=html.read()   #获取源码

    soup=BeautifulSoup(htmlcontent,'html.parser')
    meinvs=soup.find_all('h3')
    for meinv in meinvs:
        hrefurl=meinv.a.attrs['href']
        global num
        #print hrefurl

        pageurl="http://cl.chie.pw/"+hrefurl
        #print pageurl
        images=requests.get(pageurl).content
        req1 = r"input src='(.*?)'"
        urllist=re.findall(req1,images)
        if urllist==[]:
            continue
        if  "https" in urllist[0]:
            continue
        else:
            for url in urllist:
                try:
                    # filename=url.split("/")[-1]
                    # path=os.pwd()
                    # if os.path.isfile("%s/caoliu/%s" %(path,filename)):
                    #     print "%s was donwloaded" %filename
                    #     continue
                    # else:
                    urllib.urlretrieve(url, 'caoliu/%s' %url.split("/")[-1])
                    num+=1
                    print '已经下载第%d张图片'%num
                except urllib.ContentTooShortError:
                    print 'Network conditions is not good.Reloading.'
                finally:
                    break



for page in range(4,100):
    url='http://cl.chie.pw/thread0806.php?fid=16&search=&page=%d'%page
    ZhiZhuDownImag(url)