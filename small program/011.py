import sys

####Sensitive word file path
path = sys.path[0]+'\\新建文本文档.txt'
with open(path,'r',encoding="utf-8") as f:
    shuru = input()
    if shuru in f.read():
        print("Freedom")
    else:
        print("Human Rights")