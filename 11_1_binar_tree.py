class TreeNode:
    def __init__(self, node):
        self.node = node
        self.left = None
        self.right = None

def pre_order(node):
    if node:
        print(node.node, end = ' ')
        pre_order(node.left)
        pre_order(node.right)

def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.node, end = ' ')

def in_order(node):
    if node:
        in_order(node.left)
        print(node.node, end = ' ')
        in_order(node.right)

Tree = TreeNode(1)
Tree.left = TreeNode(2)
Tree.right = TreeNode(3)
Tree.left.left = TreeNode(4)
Tree.left.right = TreeNode(5)
Tree.right.left = TreeNode(6)
Tree.right.right = TreeNode(7)

print("\nBinar-Tree Pre-order parsing:")
pre_order(Tree)
print("\nBinar-Tree Post-order parsing:")
post_order(Tree)
print("\nBinar-Tree In-order parsing")
in_order(Tree)