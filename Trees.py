class Node:
    def __init__(self):
        self.left=None
        self.right=None
        self.data=None
    def inorder_traversal(self,obj): 
        if obj:
            sum=0
            self.inorder_traversal(obj.left)
            print(obj.data) #This is to print the root node 
            self.inorder_traversal(obj.right) 

    def postorder_traversal(self,Node): 
        if Node:
            self.postorder_traversal(Node.left)
               #This is to print the root node
            self.postorder_traversal(Node.right)    
            print(Node.data)   
    def preorder_traversal(self,Node): 
        if Node:
            print(Node.data)
            self.preorder_traversal(Node.left)
               #This is to print the root node
            self.preorder_traversal(Node.right)   
    def sum_of_nodes(self,Node):
        if Node is None:
            return 0
        return Node.data+ self.sum_of_nodes(Node.left)+self.sum_of_nodes(Node.right)            
    def count_nodes(self,Node):
        if Node==None:
            return 0
        return 1+self.count_nodes(Node.left)+self.count_nodes(Node.right)
    def count_leaf_nodes(self,Node):
        if Node==None:
            return 0 
        if Node.left==None and Node.right==None:
          return 1 
        return (self.count_leaf_nodes(Node.left)+self.count_leaf_nodes(Node.right))
    def height(self,Node):
        if Node==None:
            return 0
        else:
            max_height=max(self.height(Node.left),self.height(Node.right))+1
            return max_height

        
obj=Node()
obj.data=1 #root node
obj.left=Node()
obj.left.data=2
obj.right=Node()
obj.right.data=3
obj.left.left=Node()
obj.left.left.data=5
obj.left.right=Node()
obj.left.right.data=4
obj.right.left=Node()
obj.right.left.data=6
obj.right.right=Node()
obj.right.right.data=5
#print(obj.data) #root node
#print(obj.left.data) #left child
#print(obj.right.data) #right child
#print(obj.left.left.data) 
print("Inorder_traversasl")
obj.inorder_traversal(obj.left) 
print(obj.data) 
obj.inorder_traversal(obj.right)
print("Postorder_traversasl")
obj.postorder_traversal(obj.left)
obj.postorder_traversal(obj.right)
print(obj.data) 
print("Preorder_traversasl")
print(obj.data)
obj.preorder_traversal(obj.left)
obj.preorder_traversal(obj.right)
print("sum of nodes")
print(obj.sum_of_nodes(obj))
print("sum of all nodes in left subtree")
print(obj.sum_of_nodes(Node=obj.left))
print("sum of all nodes in right subtree")
print(obj.sum_of_nodes(Node=obj.right))
print("count of nodes")
print(obj.count_nodes(Node=obj))
print("count of right nodes")
print(obj.count_nodes(Node=obj.right))
print("count of left nodes")
print(obj.count_nodes(Node=obj.left))
print("count of leaf nodes")
print(obj.count_leaf_nodes(Node=obj))
print("height of tree")
print(obj.height(Node=obj))