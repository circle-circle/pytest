# -*- coding:utf-8 -*-
# author:yingwei

import urllib,urllib2
import re
from bs4 import BeautifulSoup

def getChapterList(url):
    html=urllib.urlopen(url).read()
    reg=r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
    chapterlist=re.findall(reg,html)
    #return chapterlist
    print chapterlist
    #[('34339.html','第三章 唐人的朴素是非观'）..]


def getChapter(url,chapterurl):
    urls=url.split('/')[-1]
    # print urls
    url1=url.replace(urls,chapterurl)
    # print url1

    html=urllib.urlopen('http://www.quanshuwang.com%s' %url.replace(urls,chapterurl))
    html=html.read().decode('gbk').encode('utf-8')
    # print html
    soup=BeautifulSoup(html,'html.parser')
    chapter=soup.select('div.mainContenr')
    # print type(chapter)
    # reg = r'style5\(\);</script>(.*?)<br/>'
    # chapter_title = re.findall(reg, html)
    # print chapter_title
    text=[]
    for c in chapter:

        print  type(c.get_text())


def getNovelList():
    url='http://www.quanshuwang.com/map/1.html'
    html=urllib.urlopen(url)
    htmls=html.read()
    htmls=htmls.decode('gbk').encode('utf-8')
    # print  htmls
    reg = r'<a href="(/book/.*?)" target="_blank">(.*?)</a>'
    novelist=re.findall(reg,htmls)
    # return novellist
    print novelist
    #[('/book/0/149/index.html', '帝国纵横'), ('/book/0/151/index.html', '时间尚早我们尚不老 ')....]

# url='/book/0/149/index.html'
# chapterurl='34339.html'
# getChapter(url,chapterurl)

#getNovelList()
#url="http://www.quanshuwang.com/book/0/149/index.html"
#getChapterList(url)


for novel in getNovelList():
        print novel
        noveurl=novel[0]
        novename=novel[1]
        url="http://www.quanshuwang.com" +noveurl[0]
        for chapter in getChapterList(url):
        print chapterurl=chapter[0]
        print chaptername=chapter[1]
        text_url=url.replace(url.split('/')[-1],chapterurl)
        print text_url

        # print getChapter(chapterurl,novelurl)




