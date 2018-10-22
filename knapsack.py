n=input("enter the number of limit::")
m=input("enter the bag capacity::")
arr=[]
arr2=[]
mm=m
for i in range(0,n):
	p=input("enter the probift::")
	q=input("enter the weight::")
	qt=p/q
	arr.append([p,q])
	arr2.append([p,q,qt])

print arr

arr1=arr
print "suboptimal solution for decreasing order of profits"
p=sorted(arr,reverse=True)

pi=0
for i in p:
	pii=i[0]

	wt=i[1]

	if wt<m:
	    m=m-wt
	    pi=pi+pii
	  
	else:
	    d=float(m)/float(wt)
	  
	    kk=pi+wt*d
	    break
	    
print "deceasing::",kk

	
arr1.sort(key= lambda x: x[1])
p=arr1
q=p

j=1
pii=0
for i in p:
    for j in q:
        if i[1]==j[1]:
            if i[0]>j[0]:
                swap=j[0]
                j[0]=i[0]
                i[0]=swap



for i in q:
        pi=i[0]

        wt=i[1]

        if wt<mm:
            mm=mm-wt
	 
            pii=pii+pi
            
        else:
	
	   
            d=float(mm)/float(wt)
      
            dd=pi*d
	     
	    kk1=dd+pii
	
            break

print "increments::",kk1



	 


qii=0
arr2.sort(key= lambda x: x[2],reverse=True)
ppo=arr2


for i in ppo:
        piw=i[0]

        wtw=i[1]

        if wtw<m:
            m=m-wtw
            qii=qii+piw
       
        else:
       
          
            d1=float(m)/float(wtw)
        
            dd1=piw*d1

            kkq=dd1+qii
          
            break

print "optimal pi/wi::",kk


