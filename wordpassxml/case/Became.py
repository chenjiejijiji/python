#coding=utf-8
from selenium import webdriver
import unittest
import time
import lib.commernt
import lib.Public
from page.login_page import LoginPage

class Became(unittest.TestCase):
	
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

	def test_became(self):
		#登入
		# lib.commernt.login(self.dr,self.username,self.password)
		login_page = LoginPage(self.dr)
		login_page.login(self.username,self.password)
		#发布帖子得到pen值
		pen = lib.Public.send_info(self.dr,self.data,self.text)
		print pen
		
		#查找帖子获得title
		lib.Public.find(self.dr,self.data,self.tltle_element)
		old_info = lib.Public.get_text(self.dr,self.content_element)
		print old_info
		#修改帖子（修改的内容进行比较）
		self.dr.get(self.URL + "wp-admin/post.php?post="+ pen +"&action=edit&message=6")
		lib.Public.set_variables(self.dr,self.content_main_variables)
		#查找帖子获得title
		lib.Public.find(self.dr,self.data,self.tltle_element)
		new_info = lib.Public.get_text(self.dr,self.content_element)
		#对比老的内容和新的帖子的内容的一点是不一样的
		self.assertTrue(old_info != new_info)

	def tearDown(self):
		print "End test"
		self.dr.quit()


if __name__ == '__main__':
	unittest.main()