class Node:
    def __init__(self, data):
        self.left=None
        self.right=None
        self.data=data

class BST:
    def __init__(self):
        self.root=None

    def insert(self, root, data):
        if root is None:
            return Node(data)
        if data<root.data:
            root.left=self.insert(root.left, data)
        else:
            root.right=self.insert(root.right, data)
        return root

    def insert_data(self, data):
        self.root=self.insert(self.root, data)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)

    def postorder_traversal(self, root): 
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)    
            print(root.data,end=" ")   # Print root after children (postorder)

    def preorder_traversal(self, root): 
        if root:
            print(root.data,end=" ")   # Print root before children (preorder)
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)
    def search(self,root,key):
        if root is None:
            return False
        if key==root.data:
            return True
        if key<root.data:
            #make a left call
            return self.search(root.left,key)
        if key>root.data:
            #make a right call
            return self.search(root.right,key)
        return False
    def height(self,root):
        if root==None:
            return 0
        else:
            max_height=max(self.height(root.left),self.height(root.right))+1
            return max_height
# Usage
tree = BST()
tree.insert_data(25)
tree.insert_data(20)
tree.insert_data(30)
tree.insert_data(28)
tree.insert_data(35)
tree.insert_data(18)
tree.insert_data(22)
tree.insert_data(19)
tree.insert_data(26)

print("Inorder Traversal: ")
tree.inorder(tree.root)  
print("\nPostorder Traversal: ")
tree.postorder_traversal(tree.root)  
print("\nPreorder Traversal: ")
tree.preorder_traversal(tree.root)   
print("\nKey Value: ")
print("Is 30 present in the tree",tree.search(tree.root,30))
print("Is 44 present in the tree",tree.search(tree.root,44))
print("height of tree")
print(tree.height(tree.root))