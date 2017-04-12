def cubic_generator(n):
	for i in range(n):
		yield i ** 3

x = cubic_generator(4)

#print list (x)
for n in x:
	print (n)

