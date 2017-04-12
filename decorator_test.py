def my_decorator(func):
	def wrapper(*args, **kwargs):
		print ("Before Call")
		result = func(*args, **kwargs)
		print ("after call")
		return result
	return wrapper
@my_decorator
def add(a,b):
	"our add function"
	return a+b



add(1,4)

