import urllib.request
#from bs4 import BeautifulSoup
import re

url = "http://news.163.com/world"
content = urllib.request.urlopen(url).read().decode('gbk')
c = re.compile(r'href="(.*?)</a>',re.M)
d = re.compile(r'http*')
urllist = re.findall(c,content)
for name in urllist:
    if re.match(d,name):
        print(name)