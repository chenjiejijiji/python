from selenium import webdriver
import os
import random

def random_select(what,count):
    list = [1,2,3,4,5,6]
    slice = random.sample(list,count)
    print slice[0]
    print slice[1]
    file_path = 'file:///'+os.path.abspath('1.html')

    dr = webdriver.Chrome()
    dr.get(file_path)
    
    inputs = dr.find_elements_by_tag_name('input')
    i = 0
    for input in inputs:
        if input.get_attribute('type') == what:
            while i < count:
                b = str(slice[i])
                dr.find_element_by_name(b).click()
                i =i+1

random_select('radio',2)