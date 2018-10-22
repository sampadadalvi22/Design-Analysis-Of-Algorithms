def insort(arr):
	for i in range(1,len(arr)):
	  key=arr[i]
	  j=i-1
	  while(j>=0 and arr[j]>key):
		arr[j+1]=arr[j]
		j=j-1
	  arr[j+1]=key
	print arr

arr=[]
n=input("enter the limit of array ")
for i in range(0,n):
	pp=input()
 	arr.append(pp)
insort(arr)
