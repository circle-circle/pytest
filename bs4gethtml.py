# --*-- coding:utf-8 --*--
from bs4 import BeautifulSoup
import urllib2
import urllib


num=0
def ZhiZhuDownImag(url):
    headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    req=urllib2.Request(url,headers=headers) #创建请求对象
    html=urllib2.urlopen(req,timeout=30)     #发送http请求
    htmlcontent=html.read()                  #获取源码

    soup=BeautifulSoup(htmlcontent,'html.parser')
    meinvs=soup.find_all('img')
    for meinv in meinvs:
        imaglink=meinv.get('src')
        global num
        urllib.urlretrieve(imaglink,'meinv/%d.jpg'%num)
        num+=1
        print "已经下载第%d张美图" %num

for i in range(1,100):
    url = "http://www.dbmeinv.com/?pager_offset=%d"%i
    ZhiZhuDownImag(url)