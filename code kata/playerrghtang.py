aaa,bbb,ccc=map(int,input().split())
if (aaa**2)+(bbb**2)==ccc**2 or (bbb**2)+(ccc**2)==aaa**2 or (aaa**2)+(ccc**2)==bbb**2:
	print("yes")
else:
	print("no")
