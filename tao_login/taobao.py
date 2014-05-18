#coding=utf_8
from selenium import webdriver
import unittest
import time

class Became(unittest.TestCase):
	
	def setUp(self):
		#准备工作打开火狐浏览器（要调用什么就调用什么）
		# self.dr = webdriver.Firefox()
		self.dr = webdriver.Chrome()
		# self.dr = webdriver.Ie()

		#要登入的网址
		self.URL = "http://www.taobao.com/"
		
		#用户名and密码 自己填上用户名和密码
		self.username = "tang63549880"
		self.password = "63549880"

	def test_became(self):
		self.dr.get(self.URL)
		#通过javascript定位,登入界面
		login_btn = 'document.getElementsByTagName("a")[0].click()'
		self.dr.execute_script(login_btn)
		#查找到用户名输入框
		username_text = 'document.getElementsByTagName("input").TPL_username_1.value="%s"'%(self.username)
		self.dr.execute_script(username_text)
		#点掉安全输入的框
		cafe_btn ='document.getElementsByTagName("input").J_SafeLoginCheck.click()'
		self.dr.execute_script(cafe_btn)
		time.sleep(3)
		#查找到密码的输入框
		password_text = 'document.getElementsByTagName("input").TPL_password_1.value="%s"'%(self.password)
		self.dr.execute_script(password_text)
		#点击登入按钮
		login_btn_in= 'document.getElementById("J_SubmitStatic").click()'
		self.dr.execute_script(login_btn_in)
		time.sleep(3)
		#获得text_now_username
		text_now_username = 'return document.getElementsByClassName("menu-hd")[0].textContent'
		now_username = self.dr.execute_script(text_now_username)
		#加入断言判断当前的用户名是否登入
		self.assertTrue(now_username == self.username)
		

	def tearDown(self):
		print "End test"
		self.dr.quit()


if __name__ == '__main__':
	unittest.main()