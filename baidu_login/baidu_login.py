#coding=utf_8
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
		self.URL = "http://www.baidu.com/"
		
		#用户名and密码 自己填上用户名和密码
		self.username = U"xxx"
		self.password = "xxx"

	def test_became(self):
		self.dr.get(self.URL)
		#点击百度上登入按钮
		self.dr.find_element_by_name("tj_login").click()
		#等待加载表单from
		time.sleep(5)
		#应用二次定位定位要输入的用户名
		self.dr.find_element_by_css_selector("p[id=TANGRAM__PSP_8__userNameWrapper]").find_element_by_css_selector("input[id=TANGRAM__PSP_8__userName]").send_keys(self.username)
		#应用二次定位定位要输入的密码
		self.dr.find_element_by_css_selector("p[id=TANGRAM__PSP_8__passwordWrapper]").find_element_by_css_selector("input[id=TANGRAM__PSP_8__password]").send_keys(self.password)
		#应用二次定位定位点击按钮
		self.dr.find_element_by_css_selector("p[id=TANGRAM__PSP_8__submitWrapper]").find_element_by_css_selector("input[id=TANGRAM__PSP_8__submit]").click()
		#查看是否登入可以增加时间
		time.sleep(6)

       
	def tearDown(self):
		print "End test"
		self.dr.quit()


if __name__ == '__main__':
	unittest.main()