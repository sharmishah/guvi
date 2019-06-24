ws=input()
wn=int(ws,2)
wx=wn
while 1:
	if wx&(wx-1):
		wx=wx+1
	else:
		print(wx)
		break
