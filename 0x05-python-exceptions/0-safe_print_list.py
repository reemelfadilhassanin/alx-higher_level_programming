#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
	try:
		index = 0
		i = 0
		while i < x:
			print(my_list[i], end="")
			index += 1
			i += 1
		print()
		return index
	except IndexError:
		None
		print()
		return 1
