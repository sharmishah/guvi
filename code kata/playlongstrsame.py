ab,bc=input().split()
if len(ab)==len(bc):
	print(ab+bc)
elif len(ab)>len(bc):
	cde=ab[:len(bc)]+bc
	print(cde)
else:
	cde=ab+bc[:len(ab)]
	print(cde)
