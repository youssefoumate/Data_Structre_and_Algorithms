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

    def inorder_traverse_tree(self, root):
        if root is not None:
            self.traversed_nodes.append(root)
            self.inorder_traverse_tree(root.left)
        elif self.traversed_nodes:
            t_node = self.traversed_nodes.pop()
            self.list_proc.append(t_node.data)
            self.inorder_traverse_tree(t_node.right)

tree = Tree()
tree.inorder_traverse_tree(tree.root)
print(tree.list_proc)

