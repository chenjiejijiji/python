from selenium import webdriver
import os
import time


def get_web():
    file_path = 'file:///'+os.path.abspath('2.html')
    dr = webdriver.Chrome()
    dr.get(file_path)
    a = dr.find_element_by_css_selector('a[name=baidu]').get_attribute('href')
    print a 
    dr.get(a)
    time.sleep(3)
    dr.quit()
    
get_web()