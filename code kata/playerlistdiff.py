ss=input()
rr=input()
gg=[]
if (ss.isalpha() or " " in ss) and (rr.isalpha() or " " in rr):
    ss=list(ss.split(" "))
    rs=list(rr.split(" "))
    for i in ss:
        if ss.count(i) > rr.count(i) and i not in gg:
            gg.append(i)
    for i in rr:
        if rr.count(i)>ss.count(i) and i not in gg:
            gg.append(i)
    print(*gg)
else:
    for i in ss:
        if ss.count(i)>rr.count(i) and i not in gg:
            gg.append(i)
    for i in rr:
        if rr.count(i)>ss.count(i) and i not in gg:
            gg.append(i)
    print(*gg)
