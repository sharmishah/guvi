nba=int(input())
lai=list(map(int,input().split()))
dic={}
for i in lai:
  if i in dic:
    dic[i]+=1
  else:
    dic[i]=1
lai=[]
for i in sorted(dic.items(),key=lambda kv: (kv[1],kv[0]),reverse=True):
  lai.append(i[0])
print(*lai)
