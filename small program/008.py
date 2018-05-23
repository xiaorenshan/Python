from bs4 import BeautifulSoup
import sys
import re
import urllib.request

url = "https://www.wantgoo.com/blog/article/content?blogname=44970&articleid=22"
htmlhandle = urllib.request.urlopen(url).read().decode('utf-8')
c = re.compile(r'\t(.*?)<br />',re.M)
content = c.findall(htmlhandle)
for line in content:
    print((line.replace("&ldquo;","“").replace("&rdquo;","”").replace("&nbsp;"," ")))