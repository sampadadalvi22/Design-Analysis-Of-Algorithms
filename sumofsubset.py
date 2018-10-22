def subSetSumRecur(mySet, n, goal, lis):
  if(goal==0):
    return True
  if goal<0 or n>=len(mySet) :
    return False
  if subSetSumRecur(mySet, n+1, goal - mySet[n], lis):
    lis.append(mySet[n])
    return True
  if subSetSumRecur(mySet, n+1, goal, lis):
    return True
  return False
 
mySet=[1,2,3,4,5,6,7,8,9]
goal=0
 
for i in range(len(mySet)):
  lis=[]
  subSetSumRecur(mySet[i:], 0, 9, lis)
  if len(lis)>1:
    print(lis)
