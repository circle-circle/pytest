import requests
import re
import urllib



def getUrlList(url,req):
    html = requests.get(url).content
    urlist = re.findall(req, html)


if  __name__ == "__main__":
    url=raw_input("please input url:\n")
    req=raw_input("please input req:")
    getUrl(url,req)