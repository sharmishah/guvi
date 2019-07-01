class Node:
    def __init__(self,d):
        self.ddata=d
        self.left=None
        self.right=None

def insert(root,ins):
    if ins.ddata>root.ddata and root.right!=None:
        insert(root.right,ins)
    elif ins.ddata<=root.ddata and root.left!=None:
        insert(root.left,ins)
    if ins.ddata>root.ddata and root.right==None:
        root.right=ins
        return
    elif ins.ddata<=root.ddata and root.left==None:
        root.left=ins
        return
def inorder(root):
    if root is None:
        return
    else:
        inorder(root.left)
        print(root.ddata,end=" ")
        inorder(root.right)
def lcafinder(root,nn1,nn2):
    if root is None:
        return None
    if root.ddata>nn1 and root.ddata>nn2:
        return lcafinder(root.left,nn1,nn2)
    if root.ddata<nn1 and root.ddata<nn2:
        return lcafinder(root.right,nn1,nn2)
    return root.ddata

nn=int(input())
az=list(map(int,input().split()))
l,rr1=map(int,input().split())
rr=Node(aa[0])
for i in  range(1,nn):
    nnn=Node(aa[i])
    insert(rr,nnn)
#inorder(rr)
print(lcafinder(rr,l,rr1))
