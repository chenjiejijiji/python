#coding=utf-8
import xml.dom.minidom
def xun():

	#打开xml文档
	dom = xml.dom.minidom.parse('xml.xml')

	#得到文档元素对象
	root = dom.documentElement
	print root.nodeName
	print root.nodeValue
	print root.nodeType
	print root.ELEMENT_NODE

	bb = root.getElementsByTagName('maxid')
	#print bb.nodeName
	b = bb[0]
	print b.nodeName


	bb = root.getElementsByTagName('login')
	b = bb[0]
	print b.nodeName
	print b.nodeValue