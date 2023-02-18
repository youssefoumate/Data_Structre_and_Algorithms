class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data	# data field
        self.left = left	# pointer to the left child
        self.right = right	# pointer to the right child

traversed_nodes = [] 
list_proc = [] 
def traverse_tree(root):
    if root is not None:
        traversed_nodes.append(root)
        traverse_tree(root.left)
    elif len(traversed_nodes):
        t_node = traversed_nodes.pop()
        list_proc.append(t_node.data)
        traverse_tree(t_node.right)

root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.right = Node(3)
root.right.left = Node(5)
root.right.left.left = Node(7)
root.right.left.right = Node(8)
root.right.right = Node(6)

traverse_tree(root)
print(list_proc)

