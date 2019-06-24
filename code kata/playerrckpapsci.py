aa,bb=map(str,input().split())
if aa==bb:
	print("D")
elif (aa=="R" and bb=="P") or (aa=="P" and bb=="R"):
	print("P")
elif (aa=="S" and bb=="P") or (aa=="P" and bb=="S"):
	print("S")
elif (aa=="S" and bb=="R") or (aa=="R" and bb=="S"):
	print("R")
