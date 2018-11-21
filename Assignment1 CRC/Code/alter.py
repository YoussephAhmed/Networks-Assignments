def alter( str , index ):
   
   index=index-1
  
   x = list(str)  
 
 
   if x[index]=="0":
    	x[index]="1"
   else:
    x[index]="0"
	 
   x = "".join(x)
   return x ;

#x="110111"
#m=alter (x , 3)
#print(m)
