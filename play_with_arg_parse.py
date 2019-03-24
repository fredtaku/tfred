#!/usr/bin/env python


from convert_from_string import convert_from_string

import datetime
import argparse

import logging

import os
import sys
import traceback


class PLaywithargparse:

	"""
	I use this class to play with python argparse 

	run the module on the commandline:

	you have the option to pass arguments x and/ or y


	"""

	def __init__(self, x=None, y=None):


			""" 
			initialize instance of argparse 

			and add some arguments

			"""
			self.parser = argparse.ArgumentParser()
			self.parser.add_argument("-v", "--verbose",
				help="option to Stream logging to STDOUT", action ="store_true")

			self.parser.add_argument("-x", "--x_args", help="value for x", 
				type=convert_from_string)
			
			self.parser.add_argument("-y","--y_args", help="value for y", 
				type=convert_from_string)

			self.args = self.parser.parse_args()

			"""
			add logging capability

			"""

			self.todays_date = str(datetime.datetime.now().date())
			self.filename = __class__.__name__+ ".log"+ "." + self.todays_date 

			self.abs_file_path = os.path.abspath(os.path.realpath(__file__))
			self.file_path = os.path.dirname(self.abs_file_path)
			self.logfile      = os.path.join(self.file_path, self.filename)


			self.logger = logging.getLogger(__class__.__name__)
			self.logger.setLevel(logging.DEBUG)



			self.handler = logging.FileHandler(self.logfile)
			self.formatter = logging.Formatter("%(name)s:%(module)s:%(asctime)s:%(message)s:")

			# self.stream_handler = logging.StreamHandler()

			# self.stream_handler.setFormatter(self.formatter)
			# self.logger.addHandler(self.stream_handler)

			self.handler.setFormatter(self.formatter)

			self.logger.addHandler(self.handler)


			if self.args.verbose:

				self.stream_handler = logging.StreamHandler()

				self.stream_handler.setFormatter(self.formatter)
				self.logger.addHandler(self.stream_handler)


			# add param result to use later

			self.result = None

			
			## determine the state of parameters x and y

			self.x = None
			self.y = None

			if self.args.x_args is not None:
				self.x = self.args.x_args

			else:
				self.x = x



			if self.args.y_args is not None:
				self.y = self.args.y_args

			else: 
				self.y = y



			""" 
			add defaults

			"""
			if self.x is None:
				self.x = 10


			if self.y is None:
				self.y = 2
	   
			# if self.args.verbose:

			# 	self.stream_handler = logging.StreamHandler()

			# 	self.stream_handler.setFormatter(self.formatter)
			# 	self.logger.addHandler(self.stream_handler)


   

	""" 
	add method  

	add x and y

	"""

	def add(self):

			self.logger.debug("\n Adds %d + %d : \n" %(self.x, self.y))

			self.result = self.x + self.y

			# print("The result of adding {} + {} is {}".format(self.x, self.y, self.result))

			print(f"The result of adding {self.x} + {self.y} is {self.result}")



	"""
	divide method:

	divide x/y

	"""


	def divide(self):

		try:
			self.result = self.x / self.y



		# except ZeroDivisionError:
		# 	print("\n")
		# 	self.logger.exception(" \n\n Illegal: *** division by ZERO.*** \n")  
		# 	# self.logger.debug("Exception Exception Exception")  
			
		except Exception as e:
			# print(e)
			print(traceback.print_exc())
			# self.logger.exception(e)

			# self.logger.exception("e")  
			# # self.logger.debug("Exception Exception Exception")  

			 
		else:
			print("The result of dividing {}: by :{} is {}\n".format
				(self.x, self.y, self.result))

			# print(f"The result of dividing {self.x}: by :{self.y} is {self.result}\n")

 


#create object

first_obj  = PLaywithargparse()


print("\n")

#call add method on object

first_obj.add()

print("\n")

# call divide on object

first_obj.divide()

