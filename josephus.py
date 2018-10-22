def fun1(num):
      p=2
      if(num==1):
        	print "safe number is:::1"
      else:
                for i in range(1,num):
	            p=p*2
	            if(p>=num):
		#       print p
		       break
        
                if(num==p):
	              qq=num
		else:
                      qq=p/2
		 #     print qq
		     
	              
                l=num-qq
		    
		       # print qr
	 
	        ad=2*l
	        fd=ad+1
	        print "safe number is ::",fd


n1=input("enter the number")
fun1(n1)

