aa,bb,cc=map(int,input().split())
if (aa**2)+(bb**2)==cc**2 or (bb**2)+(cc**2)==aa**2 or (aa**2)+(cc**2)==bb**2:
	print("yes")
else:
	print("no")
