#coding=utf-8

from selenium import webdriver
import unittest
import time

class Became(unittest.TestCase):
	
	def setUp(self):
		#准备工作打开火狐浏览器（要调用什么就调用什么）
		self.dr = webdriver.Firefox()
		# self.dr = webdriver.Chrome()
		# self.dr = webdriver.Ie()

		#要登入的网址
		self.URL = "http://www.discuz.net/"
		self.login = "http://www.discuz.net/connect.php?mod=login&op=init&referer=index.php&statfrom=login_simple"
		#用户名and密码 自己填上用户名和密码
		self.username = "xxx"
		self.password = "xxx"

	def test_became(self):
		#打开要登入的首页网页
		self.dr.get(self.URL)
		#id定位器定位到用户名和密码的输入框
		#5跳转到登入界面
		self.dr.get(self.login)
		time.sleep(3)
		#点击qq帐号密码登入进入iframe框
		self.dr.switch_to_frame("ptlogin_iframe")
		self.dr.find_element_by_id("switcher_plogin").click()
		#清除text中的垃圾值
		self.dr.find_element_by_id("u").clear()
		self.dr.find_element_by_id("p").clear()
		#输入用户名和密码
		self.dr.find_element_by_id("u").send_keys(self.username)
		self.dr.find_element_by_id("p").send_keys(self.password)
		#点击login——btn
		self.dr.find_element_by_id("login_button").click()

		#跳转回主页查看是否登入
		self.dr.get(self.URL)
       
	def tearDown(self):
		print "End test"
		self.dr.quit()


if __name__ == '__main__':
	unittest.main()