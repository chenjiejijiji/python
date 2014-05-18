#coding=utf-8
from selenium import webdriver
import unittest
import time
import lib.commernt
import lib.Public
from page.Loginpage import Loginpage
from page.Createpage import Createpage
from page.Findpage import Findpage

class Serach(unittest.TestCase):
	
	def setUp(self):
		self.dr = lib.commernt.Driver()
		self.username = "admin"
		self.password = "chenjiejiji!!123"
		self.title = "chenjie%s"%(time.time())
		self.URL = lib.commernt.URL()
		self.text = "chenjiejijihahah"
		self.tltle_element = ".entry-title a"
		self.content_element = ".entry-summary p"
		self.content_main_variables = "zhoujiazhe"

	def test_serach(self):
		#登入
		# lib.commernt.login(self.dr,self.username,self.password)
		login_page = Loginpage(self.dr)
		login_page.Login(self.username,self.password)

		create_page = Createpage(self.dr)
		create_page.Create(self.title,self.text)
		
		find_page = Findpage(self.dr)
		information = find_page.Find(self.title)
		new_tilte = information[0]
		new_text = information[1]
		
		self.assertTrue(new_text == self.text and new_tilte == self.title)
		# #发布帖子

		# # lib.Public.send_info(self.dr,self.data,self.text)
		# #查询帖子（加入断言帖子存在吗）

		# # get_info = lib.Public.find(self.dr,self.data,self.tltle_element)
		# self.assertTrue(get_info == self.data)

	def tearDown(self):
		print "End test"
		self.dr.quit()


if __name__ == '__main__':
	unittest.main()