import sys
import re
import urllib.request
from bs4 import BeautifulSoup

BASE_PATH = sys.path[0]
url = "https://www.piaotian.com/html/0/757/"

def GetHtml(url):
    html = urllib.request.urlopen(url).read().decode('gbk')
    soup = BeautifulSoup(html, 'lxml')
    return soup

def ChapterLinks(url):
    soup = GetHtml(url)
    links = []
    r = re.compile(r'\A[^/hj]')
    for link in soup('a'):
        result = re.match(r,link['href'])
        if result:
            links.append(url+link['href'])
    return links

def ContentHtml(url):
    c = re.compile(r'^\s{4}(.*\S)$', re.M)
    with open("content.txt",'w',encoding='utf-8') as f:
        urls = ChapterLinks(url)
        for link in urls:
            content = GetHtml(link).get_text()
            for dirty_line in content.split("\n"):
                line = re.findall(c,dirty_line)
                if line:
                    f.write("\t\t"+line[0]+"\n")
            f.write("\n\n\n")
ContentHtml(url)





