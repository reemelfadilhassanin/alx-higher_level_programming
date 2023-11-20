#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
	index = 0
	for i in range(0, x):
		x = my_list[i]
		try:
			print("{:d}".format(x), end='')
			index = index + 1
		except (ValueError, TypeError):
			pass
		print()
		return index
