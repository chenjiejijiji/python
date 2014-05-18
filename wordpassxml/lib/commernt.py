import os
from selenium import webdriver
import xml.dom.minidom

def read_xml(what):
	en = xml.dom.minidom.parse('.\\lib\\config.xml')
	read_ins = en.getElementsByTagName(what)
	to = read_ins[0].firstChild.data
	print to
	return to


def Driver():
	return os.getenv('TEST_DRIVER',webdriver.Chrome())

def URL():
	return os.getenv('TEST_EVN','http://localhost/wordpress/')

def login(dr,username,password):
	dr.get(URL() + "wp-login.php")
	dr.find_element_by_id("user_login").send_keys(username)
	dr.find_element_by_id("user_pass").send_keys(password)
	dr.find_element_by_id("wp-submit").click()


# read_xml("username")
# read_xml("password")
# read_xml("data")
# read_xml("text")
# read_xml("tltle_element")
# read_xml("content_element")
# read_xml("content_main_variables")