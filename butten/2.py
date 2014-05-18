from selenium import webdriver
from time import sleep
import os
if 'HTTP_PROXY'in os.environ: del os.environ['HTTP_PROXY']

dr = webdriver.Chrome()

first_url = 'http://www.baidu.com'
print "%s"%(first_url)

dr.get(first_url)
sleep(1)

second_url = 'http://www.news.baidu.com'
print "%s"%(second_url)
dr.get(second_url)
sleep(1)

print "back to %s"%(first_url)
dr.back()
assert dr.current_url != first_url,"error"
sleep(1)
print "forward to %s"%(second_url)
dr.forward()
sleep(1)
assert dr.current_url != second_url,"error"
dr.quit()
