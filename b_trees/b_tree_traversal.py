class Tree():

    def __init__(self):
        self.traversed_nodes = [] 
        self.list_proc = [] 
        self.root = None
        self.init_tree()

    class Node:
        def __init__(self, data=None, left=None, right=None):
            self.data = data	# data field
            self.left = left	# pointer to the left child
            self.right = right	# pointer to the right child

    def init_tree(self):
        self.root = self.Node(1)
        self.root.left = self.Node(2)
        self.root.left.left = self.Node(4)
        self.root.right = self.Node(3)
        self.root.right.left = self.Node(5)
        self.root.right.left.left = self.Node(7)
        self.root.right.left.right = self.Node(8)
        self.root.right.right = self.Node(6)

    def inorder_tree_traversal(self, root):
        if root is None:
            return   
        self.inorder_tree_traversal(root.left)
        self.list_proc.append(root.data)
        self.inorder_tree_traversal(root.right)

tree = Tree()
tree.inorder_tree_traversal(tree.root)
print(tree.list_proc)