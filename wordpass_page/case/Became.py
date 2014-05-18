#coding=utf-8
from selenium import webdriver
import unittest
import time
import lib.commernt
import lib.Public
from page.Loginpage import Loginpage
from page.Createpage import Createpage
from page.Findpage import Findpage
from page.Revisepage import Revisepage

class Became(unittest.TestCase):
	
	def setUp(self):
		self.dr = lib.commernt.Driver()
		self.username = "admin"
		self.password = "chenjiejiji!!123"
		self.title = "chenjie%s"%(time.time())
		# self.URL = "http://localhost/wordpress/"
		self.URL = lib.commernt.URL()
		self.text = "chenjiejijihahah"
		self.tltle_element = ".entry-title a"
		self.content_element = ".entry-summary p"
		self.revise_text= "zhoujiazhe"

	def test_became(self):
		#登入
		# lib.commernt.login(self.dr,self.username,self.password)
		login_page = Loginpage(self.dr)
		login_page.Login(self.username,self.password)

		creat_page = Createpage(self.dr)
		pen = creat_page.Create(self.title,self.text)

		find_page = Findpage(self.dr)
		
		information = find_page.Find(self.title)
		old_text = information[1] 
		print old_text
		revise_page = Revisepage(self.dr,pen)
		new_revise_text = revise_page.Revise(self.revise_text)
		print new_revise_text
		self.assertTrue(old_text != new_revise_text)

		#发布帖子得到pen值
		# pen = lib.Public.send_info(self.dr,self.data,self.text)
		# print pen
		
		# #查找帖子获得title
		# lib.Public.find(self.dr,self.data,self.tltle_element)
		# old_info = lib.Public.get_text(self.dr,self.content_element)
		# print old_info
		# #修改帖子（修改的内容进行比较）
		# self.dr.get(self.URL + "wp-admin/post.php?post="+ pen +"&action=edit&message=6")
		# lib.Public.set_variables(self.dr,self.content_main_variables)
		# #查找帖子获得title
		# lib.Public.find(self.dr,self.data,self.tltle_element)
		# new_info = lib.Public.get_text(self.dr,self.content_element)
		# #对比老的内容和新的帖子的内容的一点是不一样的
		# self.assertTrue(old_info != new_info)


	def tearDown(self):
		print "End test"
		self.dr.quit()


if __name__ == '__main__':
	unittest.main()