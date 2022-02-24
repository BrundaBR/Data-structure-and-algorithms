class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

class BST:
    def __init__(self):
        self.root=None
    
    def insert(self,data):
        if self.root==None:
            self.root=Node(data)
        else:
            cur=self.root
            while True:
                if data < cur.data:
                    if cur.left:
                        cur=cur.left
                    else:
                        cur.left=Node(data)
                        break
                elif data > cur.data:
                    if cur.right:
                        cur=cur.right
                    else:
                        cur.right=Node(data)
                        break

def level_order_traversal(root):
    q=[root]
    result=[]
    while q!=[]:
        s=len(q)
        for i in range(s):
            cur=q.pop(0)
            result.append(cur.data)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
    print(result)

def reverse_level_order_traversal(root):
    q=[root]
    result=[]
    while q!=[]:
        s=len(q)
        for i in range(s):
            cur=q.pop(0)
            result.insert(0,cur.data)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
    print(result)

tree=BST()
tree.insert(1)
tree.insert(2)
tree.insert(3)


level_order_traversal(tree.root)
