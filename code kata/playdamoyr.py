sba=input()
la=list(sba.split("/"))
if int(la[0])<32 and int(la[0])>0 and int(la[1])>0 and int(la[1])<13  and len(la[1])==2 and len(la[2])==4:
	print("yes")
else:
	print("no")
