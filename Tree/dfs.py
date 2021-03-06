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

def minimumDepth(root):
    s=[root]
    result=[]
    cur_depth=[]

    while s!=[]:
        
        x=s.pop()
        cur_depth.append(x.data)
        if x.right:
            s.append(x.right)
        if x.left:
            s.append(x.left)

        if x.left==None and x.right==None:
            result.append(cur_depth)
            cur_depth=[]
        
    return result


tree=BinarySearchTree()
tree.insert(8)
tree.insert(3)
tree.insert(1)
tree.insert(6)
tree.insert(4)
tree.insert(7)
tree.insert(10)
tree.insert(14)
print(minimumDepth(tree.root))