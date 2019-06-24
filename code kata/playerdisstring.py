se=input()
s12=input()
ue=se+s12
ce=0
for i in ue:
    if ue.count(i)==1:
        ce=1
    else:
        ce=0
if ce==1 and len(ue)==26:
    print("complementary")
else:
    print("non-complementary")
