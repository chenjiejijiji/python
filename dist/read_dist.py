#coding=UTF_8

chenjie_lists=[
	{"name":"chenjie   ","hunsband":"jiji   ","old":"24"},
	{"name":"zhoujiazhe","hunsband":"chenjie","old":"25"},
]


def read_dist():
	for chenjie_list in chenjie_lists:
		print "******************"
		print chenjie_list["name"]
		print chenjie_list["hunsband"]
		print chenjie_list["old"]
		print "________END_______"

if __name__ == '__main__':
	read_dist()