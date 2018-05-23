import sys
a = sys.path[0]+'\\新建文本文档.txt'
result = dict()
with open(a,'r') as f:
    for word in f.read():
        if word.lower() in result.keys():
            result[word.lower()] = result[word.lower()] + 1
        else:
            result[word.lower()] = 1
for key,vales in result.items():
    print (key,':', vales)