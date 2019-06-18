try:
	U11=int(input())
	if(U11>=-2**15+1  and U11<=2**15+1):
	    print ("INT")
	elif U11>=-2**31+1 and U11<=2**31+1:
	    print("LONG")  
	else:
	    print ("LONG LONG")
except ValueError:
	print("invalid")
