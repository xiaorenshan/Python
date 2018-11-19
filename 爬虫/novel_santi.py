import sys
import urllib.request
import re
from bs4 import BeautifulSoup

url = "http://www.luoxia.com/santi/"

def GetHtml(url):
    html = urllib.request.urlopen(url).read().decode('utf-8')
    return html

a = re.compile(r'santi/(.+?)\.htm',re.M)
Content = GetHtml(url)
number = re.findall(a,Content)

with open("santi.txt",'w',encoding='utf-8') as f:
    for i in number:
        new_url = url+i+"/htm"
#        print(new_url)
        try:
            soup = BeautifulSoup(GetHtml(new_url),"lxml")
            title = soup.find(class_="post-title").string
            content = soup.find(id="nr1").get_text()
        finally:
            f.write(title)
            f.write(content)
            f.write("\n\n\n")