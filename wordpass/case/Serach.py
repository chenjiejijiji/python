#coding=utf-8
from selenium import webdriver
import unittest
import time
import lib.commernt
import lib.Public

class Serach(unittest.TestCase):
	
	def setUp(self):
		self.dr = lib.commernt.Driver()
		self.username = "admin"
		self.password = "chenjiejiji!!123"
		self.data = "chenjie%s"%(time.time())
		self.URL = lib.commernt.URL()
		self.text = "chenjiejijihahah"
		self.tltle_element = ".entry-title a"
		self.content_element = ".entry-summary p"
		self.content_main_variables = "zhoujiazhe"

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