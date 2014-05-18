#coding=utf-8
from selenium import webdriver
import unittest
import time
import lib.commernt
import lib.Public

class Serach(unittest.TestCase):
	
	def setUp(self):
		self.dr = lib.commernt.Driver()
		self.URL = lib.commernt.URL()
		self.username = lib.commernt.read_xml("username")
		self.password = lib.commernt.read_xml("password")
		self.text = lib.commernt.read_xml("text")
		self.tltle_element = lib.commernt.read_xml("tltle_element")
		self.content_element = lib.commernt.read_xml("content_element")
		self.content_main_variables = lib.commernt.read_xml("content_main_variables")
		self.data = "chenjie%s"%(time.time())

	def test_serach(self):
		#登入
		lib.commernt.login(self.dr,self.username,self.password)

		#发布帖子

		lib.Public.send_info(self.dr,self.data,self.text)
		#查询帖子（加入断言帖子存在吗）

		get_info = lib.Public.find(self.dr,self.data,self.tltle_element)
		self.assertTrue(get_info == self.data)

	def tearDown(self):
		print "End test"
		self.dr.quit()


if __name__ == '__main__':
	unittest.main()