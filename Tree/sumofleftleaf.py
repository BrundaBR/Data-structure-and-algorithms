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

def checkleaf(root):
    if root==None:
        return False
    if root.left==None and root.right==None:
        return True
    return False


def basefunction(root):
    su=[]
    if root==None:
        return None
    
    if checkleaf(root.left):
        su.append(root.left.data)
    leftchild=basefunction(root.left)
    rightchild=basefunction(root.right)
    return sum(su)   







tree=BinarySearchTree()
tree.insert(2)
tree.insert(1)
tree.insert(3)
print(basefunction(tree.root))
