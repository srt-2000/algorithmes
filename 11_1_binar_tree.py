class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def pre_order(self, node):
        if node:
            print(node.val, end=' ')
            self.pre_order(node.left)
            self.pre_order(node.right)

    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.val, end=' ')

    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.val, end=' ')
            self.in_order(node.right)

Tree = TreeNode(1)
Tree.left = TreeNode(2)
Tree.right = TreeNode(3)
Tree.left.left = TreeNode(4)
Tree.left.right = TreeNode(5)
Tree.right.left = TreeNode(6)
Tree.right.right = TreeNode(7)

print("\nBinary-Tree Pre-order parsing:")
Tree.pre_order(Tree)
print("\nBinary-Tree Post-order parsing:")
Tree.post_order(Tree)
print("\nBinary-Tree In-order parsing")
Tree.in_order(Tree)