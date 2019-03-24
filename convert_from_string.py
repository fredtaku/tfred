#!/usr/bin/env python



def my_type(s):

	if s.isdigit():
		return int(s)

	elif isinstance(float(s), float):
		return float(s)



def convert_from_string(s):
	try:
		return int(s)

	except Exception:
		return float(s)





if __name__=='__main__':
	import argparse

	parser = argparse.ArgumentParser()

	parser.add_argument("-s", "--st")
	args = parser.parse_args()

	print(convert_from_string(args.st))

