class counter_try(object):
	def __init__(self, low, high):
		self.current = low
		self.high = high
	def __iter__(self):
		return self
	def __next__(self):
		if self.current > self.high:
			raise StopIteration
		else:
			self.current +=1
			return self.current - 1

	def next(self):
		return self.__next__()


x = counter_try(1,10)
for i in x :
	print (i)
