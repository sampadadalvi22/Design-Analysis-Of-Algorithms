import time
def recursive(n):
		if n==1:
		     return n
		else:
		     return n*recursive(n-1)	   
def iterative(n):
	fact=1
	for i in range(1,n+1):
		fact=fact*i
        return fact
print "fact programs check time using time clock function..."		
n=input()
st=time.clock()	
d1=iterative(n)
print d1
print "Iterative measure time is::",time.clock()-st
st1=time.clock()
dd=recursive(n)
print dd
print "Recursive measure time is::",time.clock()-st1
