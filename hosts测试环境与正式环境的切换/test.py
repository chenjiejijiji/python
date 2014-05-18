#coding=utf-8
from selenium import webdriver
import os

def test():
	dr = webdriver.Chrome()
	URL = read(0)
	dr.get(URL)
	URL = read(1)
	dr.get(URL)

	

def read(what):
	line = open('config.txt','r')
	result = list()
	for info in line.readlines():
		print info
		result.append(info)
		#return result
	infoemation = result[what]
	return 	infoemation	
	line.close()

test()
