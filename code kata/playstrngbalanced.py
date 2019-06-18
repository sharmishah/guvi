s=input()
li=list(s)
if(li[0]=='(' and li[-1]==')'):
    if(li.count('(')==li.count(')')):
        print("yes")
    else:
        print("no")
else:
    print("no")
