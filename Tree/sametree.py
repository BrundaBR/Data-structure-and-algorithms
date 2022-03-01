from operator import truediv


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


def Breadthfirstsearch(root):
    q=[root]
    result=[]
    while q!=[]:
        size=len(q)
        for i  in range(size):
            cur=q.pop(0)
            result.append(cur.data)
            if cur.left:
                q.append(cur.left)
            else:
                result.append("Null")
            if cur.right:
                q.append(cur.right)
            result.append("Null")

    return result

def SameTree(tree1,tree2):
    if tree1==tree2:
        return True
    else:
        return False

tree=BinarySearchTree()
tree1=BinarySearchTree()

tree.insert(1)
tree.insert(2)
# tree.insert(1)
# tree.insert(6)
# tree.insert(4)
# tree.insert(7)
# tree.insert(10)
# tree.insert(14)

tree1.insert(1)
# tree1.insert()
tree1.insert(2)
# tree1.insert(6)
# tree1.insert(4)
# tree1.insert(7)
# tree1.insert(10)
# tree1.insert(14)

x=Breadthfirstsearch(tree.root)
y=Breadthfirstsearch(tree1.root)
print(SameTree(x,y))