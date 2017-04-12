#x=[2,3,5,6]
#y=[4,3,5,6]
#func=map(lambda x:x%2 ,x)
#print func

#x=[0,1,1,2,3,5,8,13,21,34,5]
#func=filter(lambda x : x %2 , x)
#print ('elements which cannot be divide by:', func)
#
#
#funct=filter(lambda x : x %2==0 , x)
#print ('elements which can be divided:', funct)

#x=[2,5,8,2,4,1]
#z=reduce(lambda x,y:x+y,[2,5,8,2,4,1])
#print z
#
#func=lambda a,b: a if (a>b) else b
#x=reduce(func , [42,56,57,87,95,564])
#print x

#items=[1,2,3,4,5]
#def sqr(x):
#	return (x ** 2)
#def cube(x):
#	return (x ** 3)
#y=(map(sqr, items))
#print y

#z=map(lambda x: x ** 2,items)
#print z
#for i in z:
#	print i
#y=[sqr, cube]
#for i in range(5):
#	z=map(lambda x: x(i), y)
#	print z
z=[4, 4, 9, 12, 13, 2, 7, 9, 11, 11,1]

def prime_test(x):
	if (x==1):
		return False
	elif (x==2):
		return True;
	else:
		for i in range(2,x):
		       if (x%i ==0):
				return False
		return True
#print (prime_test(z))	
r=filter(prime_test, z)
print (r)


j=reduce(lambda x,y : x-y , z)
print j



