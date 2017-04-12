def divide_checker(funct):
	def inner_func(a,b):
		print ("going to divide",a, "and" ,b)
		if b==0:
			x="Cannot divide by 0"
			
			return x 
		return funct(a,b)
	return inner_func

@divide_checker
def divide(a,b):
	return a/b


x=divide(2,0)

print x

