class Tree:
    def __init__(self, node, left=None, right=None):
        self.node = node
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.node)

def total(full_tree):
    if full_tree is None:
        return 0
    return total(full_tree.left) + total(full_tree.right) + full_tree.node

def pre_order_tree(full_tree):
    if full_tree is None: return
    print(full_tree.node)
    pre_order_tree(full_tree.left)
    pre_order_tree(full_tree.right)

tree = Tree(1, Tree(2, Tree(4), Tree(5)), Tree(3, Tree(6), Tree(7)))
pre_order_tree(tree)