aa,bb,cc=map(int,input().split())
if aa+bb<=cc or cc+bb<=aa or aa+cc<=bb:
	print("no")
else:
	print("yes")
