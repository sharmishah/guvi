ad=int(input())
td=1
while(td<=ad and td*2<=ad):
    td=td*2

if(td==ad):
    print("0")
else:    
    print(ad-td)
