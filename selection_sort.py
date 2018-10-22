def selection(arr):
	for i in range(0,len(arr)):
	      j=i
	      for j in range(j,len(arr)):
		  if arr[i]>arr[j]:
			temp=arr[i]
			arr[i]=arr[j]
			arr[j]=temp
        print arr
n=input("enter the limit")
arr=[]
for i in range(0,n):
	p=input()
	arr.append(p)
selection(arr)
