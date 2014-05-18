#coding=UTF_8
import csv

#读取本地csv文件

datas = csv.reader(file('information_config.csv','r'))

for data in datas:
	print data[0]
	print data[1]
	print data[2]