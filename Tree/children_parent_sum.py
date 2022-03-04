su=0
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
    

    def helper(self,root,lis):
        if root==None:
            return None
        if root.right:
            lis.append(root.right.data)
        if root.left:
            lis.append(root.left.data)
        if root.data == sum(lis):
            return 1
        else:
            
            self.helper(root.left,lis) 
            self.helper(root.right,lis)
            return 0
        
    def Base(self,root):
        sum_val=[]
        if root==None:
            return None
        else:
            return self.helper(root,sum_val)
            
         



tree=BinarySearchTree()
tree.insert(4)
tree.insert(1)
tree.insert(3)
print(tree.Base(tree.root))
