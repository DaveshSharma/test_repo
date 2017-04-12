def star_print(funct):
	def inner_func(*args, **kwargs):
		print ("*" * 30)
		funct(*args, **kwargs)
		print ("*" * 30)
	return inner_func
def percent_print(func):
	def inner_funct(*args, **kwargs):
		print ("%" * 30)
		func(*args, **kwargs)
		print ("%" * 30)
	return inner_funct




@percent_print
@star_print
def printer(msg):
	print(msg)
printer("hey")
