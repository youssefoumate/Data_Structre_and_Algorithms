class Tree():

    def __init__(self):
        self.traversed_nodes = [] 
        self.list_proc = [] 
        self.temp = []
        self.bottom_view = []

    class Node:
        def __init__(self, data=None, left=None, right=None):
            self.data = data	# data field
            self.left = left	# pointer to the left child
            self.right = right	# pointer to the right child

    def init_tree(self, v_root):
        root = self.Node(v_root)
        root.left = self.Node(2)
        root.left.left = self.Node(4)
        root.right = self.Node(3)
        root.right.left = self.Node(5)
        root.right.left.left = self.Node(7)
        root.right.left.right = self.Node(8)
        root.right.right = self.Node(6)
        return root

    def inorder_tree_traversal(self, root):
        if root is None:
            return   
        self.inorder_tree_traversal(root.left)
        self.list_proc.append(root.data)
        self.inorder_tree_traversal(root.right)

    def preorder_tree_traversal(self, root):
        if root is None:
            return
        self.list_proc.append(root.data)
        self.preorder_tree_traversal(root.left)
        self.preorder_tree_traversal(root.right)

    def postorder_tree_traversal(self, root):
        if root is None:
            return
        self.postorder_tree_traversal(root.left)
        self.postorder_tree_traversal(root.right)
        self.list_proc.append(root.data)

    def cmp_trees(self, root1, root2):         
        if root1 is None or root2 is None:
            return
        self.cmp_trees(root1.left, root2.left)
        if root1.data != root2.data:
            return False
        self.cmp_trees(root1.right, root2.right)
        return True
    
    def naive_tree_bottom_view(self, root):
        # traverse the tree (inorder)
        # a hidden node has a right.left child or left.right child
        if root is None:
            return
        self.naive_tree_bottom_view(root.left)
        self.list_proc.append(root.data)
        if root.left is not None:
            if root.right is not None:
                self.temp.append(root.data)
        self.naive_tree_bottom_view(root.right)
        self.bottom_view = [n for n in self.list_proc if n not in self.temp]
        
        

tree = Tree()
root1 = tree.init_tree(1)
root2 = tree.init_tree(7)
#print(tree.cmp_trees(root1, root2))
tree.naive_tree_bottom_view(root1)
print(tree.bottom_view)