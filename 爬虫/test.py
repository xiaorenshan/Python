class makeHtmlTagClass(object):
    def __init__(self, tag, css_calss=""):
        self.tag = tag
        self._css_class = "css_calss='{}'".format(css_calss) if css_calss !="" else ""
    def __call__(self, fn):
        def wrapper(*args):
            return "<"+self.tag+" "+ self._css_class+">"+fn(*args)+"<"+self.tag+">"
        return wrapper

@makeHtmlTagClass(tag="b", css_calss="bild_css")
@makeHtmlTagClass(tag="i", css_calss="italic_css")
def hello(name):
    return "Hello, {}".format(name)

result = hello("zhouxian")
print (result)

