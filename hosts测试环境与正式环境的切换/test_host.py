#coding=utf-8
import os

#内网测试环境
insides =['http://www.baidu.com',
			'http://www.qq.com']

#外网测试环境
outsides =['http://www.youku.com',
			'http://www.tudou.com']

def insides_test():
	output = open('config.txt','w')
	for insid in insides:
		print insid
		output.write(insid)
		output.write('\n')
	output.close()

def outsides_test():
	output = open('config.txt','w')
	for outside in outsides:
		print outside
		output.write(outside)
		output.write('\n')
	output.close()

if __name__ == "__main__":
	#insides_test()
	outsides_test()

