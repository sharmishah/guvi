vs=input()
vr=input()
vg=[]
if (vs.isalpha() or " " in vs) and (vr.isalpha() or " " in vr):
    vs=list(vs.split(" "))
    vr=list(vr.split(" "))
    for i in vs:
        if vs.count(i) > vr.count(i) and i not in vg:
            vg.append(i)
    for i in vr:
        if vr.count(i)>vs.count(i) and i not in vg:
            vg.append(i)
    print(*vg)
else:
    for i in vs:
        if vs.count(i)>vr.count(i) and i not in vg:
            vg.append(i)
    for j in vr:
        if vr.count(j)>vs.count(j) and j not in vg:
            vg.append(j)
    print(*vg)
