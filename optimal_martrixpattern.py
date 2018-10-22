def check(arr):
	if(len(arr)==1):
		pp=arr[0]
		print "optimal marge sort values::",pp
		
	else:
		
		p1=arr[0]
		p2=arr[1]
		arr.remove(p1)
		arr.remove(p2)
		pp=p1+p2
		arr.append(pp)
		arr.sort()
		check(arr)
arr=[]
n=input("enter the limit")
for i in range(0,n):
	p=input()
	arr.append(p)
check(arr)


