#!/usr/bin/python3
import sys


def safe_function(fct, *args):
	try:
		fct(*args)
	except BaseException as e:
		print("Exception: {}".format(e), file=sys.stderr)
		return None
	finally:
		return  fct(*args)
