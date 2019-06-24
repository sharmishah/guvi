str11=input()
str22=input()
arr11=[]
arr22=[]
if (str11.isalpha() or " " in str11) and (str22.isalpha() or " " in str22):
    str11=list(str11.split(" "))
    str22=list(str22.split(" "))
    for i in str22:
        if str22.count(i) > str11.count(i) and i not in arr11:
            arr11.append(i)
    for i in arr11:
    	if(i!=" "):
    		print("1:"+i)
    for i in str11:
        if str11.count(i)>str22.count(i) and i not in arr22:
            arr22.append(i)
    for i in arr22:
    	if(i!=" "):
    		print("2:"+i)
else:
    for i in str22:
        if str22.count(i)>str11.count(i) and i not in arr11:
            arr11.append(i)
    for i in arr11:
    	if(i!=" "):
    		print("1:"+i)
    for j in str11:
        if str11.count(j)>str22.count(j) and j not in arr22:
            arr22.append(j)
    for i in arr22:
    	if(i!=" "):
    		print("2:"+i)
