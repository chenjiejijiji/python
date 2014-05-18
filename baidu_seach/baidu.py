#coding=UTF_8

from selenium import webdriver
import time
import unittest

class Became(unittest.TestCase):
	
	def setUp(self):
		#准备工作打开火狐浏览器（要调用什么就调用什么）
		# self.dr = webdriver.Firefox()
		self.dr = webdriver.Chrome()
		#要登入的网址
		self.URL = "http://www.baidu.com/"
		self.serch_text = "webdriver"

	def test_became(self):
		#输入网址
		self.dr.get(self.URL)
		#最大化浏览器
		self.dr.maximize_window()
		#停顿30秒
		time.sleep(3)
		self.dr.find_element_by_id('kw1').send_keys(self.serch_text)
		self.dr.find_element_by_id('su1').click()
		#停顿300秒
		time.sleep(300)
		
	def tearDown(self):
		print "End test"
		self.dr.quit()


if __name__ == '__main__':
	unittest.main()

