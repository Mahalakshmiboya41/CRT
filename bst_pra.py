class Node:
    def __init__(self):
        self.left=None
        self.right=None
        self.data=None
class BST:
    def __init__(self):
        self.root=None
    
    def insert(self,obj,root,data):
        if root==None:
            return Node(data)
        if obj.root.data>obj.data:
           return self.insert(obj.left)
        else:
            return self.insert(obj.right)
        

obj=Node()
obj.root=Node()
obj.root.data=25
obj.left=Node()
obj.data=20