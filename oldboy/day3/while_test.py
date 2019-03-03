# -*- coding:utf-8 -*-

row = 1

while row <= 5:

	# 每一行要打印的星星就是和当前的行数是一致的
	# 增加一个小的循环，专门负责当前行中 每一列的星星的显示

	col = 1

	while col <= row:
		
		# print("%d" % col)

		print("*", end="")

		col += 1

	# print("第 %d 行" %row)
	print("")
	row += 1