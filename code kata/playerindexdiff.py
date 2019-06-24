xax=int(input())
ax=list(map(int,input().split()))
bx=sorted(ax)
print(ax.index(bx[len(bx)-1])-ax.index(bx[0]))
