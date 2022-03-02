class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    

class BinarySearchTree:
    def __init__(self) -> None:
        self.root=None
    

    def insert(self,value):
        if self.root==None:
            self.root=Node(value)
        else:
            cur=self.root
            while True:
                if value < cur.data:
                    if cur.left:
                        cur=cur.left
                    else:
                        cur.left=Node(value)
                        break
                elif value > cur.data:
                    if cur.right:
                        cur=cur.right
                    else:
                        cur.right=Node(value)
                        break
#Functions on Tree   
'''def printTree(root):
    if root:
        
        printTree(root.left)
        printTree(root.right)
        print(root.data,end="->")'''

def largetVal(root):
    q=[root]
    result=[]
    large=[]
    while q!=[]:
        size=len(q)
        l=-1
        for i in range(size):
            cur=q.pop(0)
            if cur.data >l:
                l=cur.data
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        large.append(l)
        
    for i in result:
        x=max(i)
        large.append(x)
    return large




tree=BinarySearchTree()
tree.insert(8)
tree.insert(3)
tree.insert(1)
tree.insert(6)
tree.insert(4)
tree.insert(7)
tree.insert(10)
tree.insert(14)
print(largetVal(tree.root))