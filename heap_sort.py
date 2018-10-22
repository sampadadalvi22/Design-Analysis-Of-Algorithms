def heapify(data, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
 
    if l < n and data[i] < data[l]:
        largest = l
 
  
    if r < n and data[largest] < data[r]:
        largest = r
 

    if largest != i:
        data[i],data[largest] = data[largest],data[i]
 
        heapify(data, n, largest)
 

def heapSort(data):
    n = len(data)
 
   
    for i in range(n, -1, -1):
        heapify(data, n, i)
 
    
    for i in range(n-1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)
  
  
n=input()
numList=[]
for i in range(0,n):
	p=input()
	numList.append(p)
print('Before sort:')
print(numList)

heapSort(numList)
print('After sort:')
print(numList)

