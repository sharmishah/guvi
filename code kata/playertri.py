aaa,bbb,ccc=map(int,input().split())
if aaa+bbb<=ccc or ccc+bbb<=aaa or aaa+ccc<=bbb:
	print("no")
else:
	print("yes")
