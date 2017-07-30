# --*--  coding:utf-8 --*--
import urllib2
from bs4 import BeautifulSoup


def getUrlList(url):
    html=urllib2.urlopen(url)
    html=html.read()
    return html

url='http://www.pythontab.com/html/pythonhexinbiancheng/index.html'
url_list=[url]
for i in range(2,22):
    url_list.append('http://www.pythontab.com/html/pythonhexinbiancheng/%s.html' %i)
for j in url_list:
    html=getUrlList(j)
    soup=BeautifulSoup(html,'html.parser')
    title_list=soup.select('#catlist > li > a')
    for title in title_list:
        tname = title.get_text().replace('*','').replace('/','').replace(',','')  #获取标题名称
        links = title.get('href') #获取内容url
        title_p=getUrlList(links)
        soup1=BeautifulSoup(title_p,'html.parser')
        jc=soup1.select('div.content > p ')
        text=[]
        for k in jc:
             text.append(k.get_text().encode('utf-8'))
        print "正在下载 %s" %tname
        with open('pythontab/%s.txt' %tname,'wb+') as f:
            for a in text:
                f.write(a)




