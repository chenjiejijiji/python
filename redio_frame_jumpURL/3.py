from selenium import webdriver
import os
import time

def frame():
	fail_path = "file:///"+os.path.abspath("frame.html")

	dr = webdriver.Chrome()
	dr.get(fail_path)

	frame = dr.find_element_by_css_selector("body > div > iframe")
	dr.switch_to_frame(frame)
	dr.find_element_by_css_selector("#kw1").send_keys('webdriver')
	
	dr.find_element_by_css_selector("#su1").click()
	time.sleep(5)
	dr.switch_to_default_content()
	dr.quit()

frame()