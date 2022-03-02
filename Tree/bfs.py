class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree:
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


def bfs(root):
    q=[root]
    result_q=[]
    while q!=[]:
        siz=len(q) 
        current_level=[]
        for i in range(siz):
            # pop element from q & add it to stack
            ele=q.pop(0) 
            current_level.append(ele.data)
            # # add it to q
            if ele.left:
                q.append(ele.left)  

            if ele.right:
                q.append(ele.right)  

        result_q.append(current_level)
    return result_q



def depthfirstsearch(root):
	if root is None:
		return 
	stack=[root]
	result=[] #
	while stack!=[]:#
		current=stack.pop()# 
		result.append(current.data)
		if current.left:
			stack.append(current.left)
		if current.right:
			stack.append(current.right)
	print(result)


tree=Tree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)

# print(bfs(tree.root))
depthfirstsearch(tree.root)