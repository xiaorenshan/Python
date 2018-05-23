import sys
import re

#####Sensitive word file path
path = sys.path[0]+"\\新建文本文档.txt"
Sensitive_word = []
result=""
mark = ""
with open(path,'r',encoding="utf-8") as f:
    words = f.read()
shuru = input()
for word in words.split(" "):
    if re.findall(word,shuru):
        Sensitive_word.append(word)
        mark = 0
if mark == 0:
    a = "|".join(Sensitive_word)
    result = re.sub(a,"**",shuru)
else:
    result = shuru
print(result)