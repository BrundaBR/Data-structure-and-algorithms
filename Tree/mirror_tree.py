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
def printTree(root):
    if root:
        print(root.data,end="->")
        printTree(root.left)
        printTree(root.right)
        

def mirrorTree(root):
    #check cases
	def InvertTree(node):

		if node == None:

			return None

		InvertTree(node.left)

		InvertTree(node.right)
        #swapping
		node.left, node.right = node.right, node.left

	InvertTree(root)

	return root



tree=BinarySearchTree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
printTree(tree.root)
nodenew=mirrorTree(tree.root)
printTree(tree.root)

