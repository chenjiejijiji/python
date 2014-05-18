from selenium import webdriver
from time import sleep
import os

dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('from.html')

dr.get(file_path)
#print dr.find_element_by_tag_name('form').get_attribute('class')

#print dr.find_element_by_tag_name('div').get_attribute('class')

e = dr.find_element_by_class_name('controls')
dr.execute_script('$(arguments[0]).fadeOut().fadeIn()', e)
