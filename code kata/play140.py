ps=input()
if all(i=="a" or i=="b" for i in ps):
    print("yes")
elif all(i=="a" for i in ps):
    print("yes")
elif all(i=="b" for i in ps):
    print("yes")
else:
    print("no")
