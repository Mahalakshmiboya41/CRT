class Node:
    def _init_(self, val):
        self.val = val
        self.left = None
        self.right = None

def create_tree(values, index):
    if index >= len(values) or values[index] is None:
        return None

    node = Node(values[index])
    node.left = create_tree(values, 2 * index + 1)
    node.right = create_tree(values, 2 * index + 2)
    return node

def are_identical(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    return (root1.val == root2.val and
            are_identical(root1.left, root2.left) and
            are_identical(root1.right, root2.right))

def main():
    n1 = int(input())
    values1 = list(map(int, input().split()))
    n2 = int(input())
    values2 = list(map(int, input().split()))

    root1 = create_tree(values1, 0)
    root2 = create_tree(values2, 0)

    if are_identical(root1, root2):
        print("The given binary trees are identical")
    else:
        print("The given binary trees are not identical")

main()