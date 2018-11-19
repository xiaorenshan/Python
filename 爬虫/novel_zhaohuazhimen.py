import urllib.request
import sys
import re
from bs4 import BeautifulSoup

url = 'https://www.piaotian.com/html/6/6062/3291586.html'
base_path = sys.path[0]
def GetHtml(url):
    dirty_html = urllib.request.urlopen(url).read().decode('gbk')
    soup = BeautifulSoup(dirty_html, 'lxml')
    return soup
def GetResult(url):
    soup = GetHtml(url)
    title = soup.h1.get_text().split(' ' ,1)[1]
    content = soup.find_all('div', "content")
    print(content)
GetResult(url)