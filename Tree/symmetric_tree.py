from ast import Pass


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

def symmetric_tree(root):
    def helper(p,q):
        if p==None and q==None:
            return True
        if p==None or q==None:
            return False
        if p.data!=q.data:
            return False
        return helper(p.left,q.right) and helper(p.right,q.left)
    helper(root.left,root.right)
    



tree=BinarySearchTree()
tree.insert(1)
tree.insert(2)
tree.insert(3)

print(symmetric_tree(tree.root))