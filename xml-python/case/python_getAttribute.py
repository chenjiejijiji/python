#coding=utf-8
import xml.dom.minidom
def xun():
	#打开xml文档
	#dom = xml.dom.minidom.parse('F:\\xml-python\\case\\xml.xml')
	dom = xml.dom.minidom.parse('.\\case\\xml.xml')

	root = dom.documentElement

	cc = dom.getElementsByTagName('caption')
	c1 = cc[0]
	print c1.firstChild.data

	# c2 = cc[1]
	# print c2.firstChild.data

	c3 = cc[2]
	print c3.firstChild.data

xun()