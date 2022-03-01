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

def heightoftree(root):
    if root==None:
        return 0
    #recursive call
    left=heightoftree(root.left)
    right=heightoftree(root.right)

    #return 
    return min(left,right)+1



tree=BinarySearchTree()
tree.insert(8)
tree.insert(3)
tree.insert(1)
tree.insert(6)
tree.insert(4)
tree.insert(7)
tree.insert(10)
tree.insert(14)
print(heightoftree(tree.root))