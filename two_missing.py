n=input()
arr=[]
for i in range(0,n-2):
	p=input()
	arr.append(p)
p1=max(arr)
q1=min(arr)
flag=0
ar=[]
for i in range(q1,p1+1):
	for j in range(0,len(arr)):
		if arr[j]==i:
		   
		   flag=0
		   break
		   
		else:
		   flag=1  	
		
	if flag==1:
		ar.append(i)

if(len(ar)==0):
	print "missing number is",q1-1
	print "missing number is",p1+1
else:
        for i in ar:
            print "missing number is",i	   
