def matrixChainMulti():
    num=int(input('how many matrix:'))
    mat_dim=[]
    for i in range(num+1):
        print "enter the dia:",i+1
        mat_dim.append(int(input()))
  
    matrix=[]
    for i in range(num):
        matrix.append([0]*num)
   
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
             if i!=j:
                matrix[i][j] ='-'
    n=num
    for i in range(num-2,-1,-1):
        for j in range(n-1,num):
             if(j>i):
                 min1=[]
              
                 for k in range(i,j):
                  
                     sum1=matrix[i][k]+matrix[k+1][j]+(mat_dim[i]*mat_dim[k+1]*mat_dim[j+1])
                     min1.append(sum1)
                   
                 if(len(min1)>1):
                     val=min(min1)
               
                     matrix[i][j] = val
                 else:
                     val=sum1
                  
                     matrix[i][j] = val
        n=n-1
    print "matrixchain multipiction::"
    for i in matrix:
	print i
matrixChainMulti()


