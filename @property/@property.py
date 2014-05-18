#coding=UTF_8

class file_read():

	def __init__(self):
		file_one = self.read
	
	@property
	def read(self):
		open_file = open("chenjie.txt",'r')
		new_file = open_file.read()
		print new_file
		open_file.close()
		return new_file


file_read()
