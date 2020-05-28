from lxml import etree

#读取一个xml文件：在文件里借助lxml对文件进行搜索和元素定位

#加载xml文件
xml=etree.parse('./class.xml')
#寻找路径，定位元素
nodes=xml.xpath("//xpath")
#获取元素的属性
#nodes.get['buonds']




#封装一个定位元素的方法
def find_element_by_text(text):
    nodes=xml.xpath('//dddd=%s'%text)
    if len(nodes)==1:
        return nodes[0]
    elif len(nodes)>1:
        raise Exception("属性不唯一")
    else:
        raise Exception("no such element found by ddd%s"%text)
