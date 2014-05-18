import os
from selenium import webdriver

def Driver():
	return os.getenv('TEST_DRIVER',webdriver.Chrome())

def URL():
	return os.getenv('TEST_EVN','http://localhost/wordpress/')

# def login(dr,username,password):
# 	dr.get(URL() + "wp-login.php")
# 	dr.find_element_by_id("user_login").send_keys(username)
# 	dr.find_element_by_id("user_pass").send_keys(password)
# 	dr.find_element_by_id("wp-submit").click()