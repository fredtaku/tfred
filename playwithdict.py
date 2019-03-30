#!/usr/bin/env python


from collections import defaultdict

#defaultdict implements a default value for a dict key in case key is missing.

names ="Mike,John,Mike,Anna,Mike,John,John,Mike,Mike,Britney,Smith,Anna,Smith".split(',')

print()
print()
print(names)

#set default_factory
mydict = defaultdict(int)


print()
print()


for name in names:

	mydict[name] +=1
	

print(mydict)


print()
print()



#create a dict class that provide a callable 


class MyDict(dict):

	def __init__(self, factory):

		self.factory = factory

	


#__getitem__ will call __missing__ in case there is no key


	def __missing__(self, key):

		self[key] = self.factory(key)
		# self[key] = '{} {}'.format(str(key), self.family_name)

		return self[key]


#factory method takes a key, which is the 
# a family member's first name and create 
#and concatenate the name to family name.


def my_factory(key):
	family_name = "My_Family_Name"
	# return "{} {}".format(str(key), family_name)
	return f"{str(key)}  {family_name}"


family_ = "first_son_name ,second_son_name, dad_name".split(',')


# counterdict=MyDict(my_factory)
counterdict=MyDict(my_factory)
# counterdict=defaultdict(int)
# counterdict=defaultdict(str)

for name in family_:

	counterdict[name] 



print(counterdict)	


print()
print()





