class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

# Insertion
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.value < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

# search
def search(root, key):
    if root is None or root.value == key:
        return root
    if root.value < key:
        return search(root.right, key)
    return search(root.left, key)

# deletion
def delete_node(root, key):
    if root is None:
        return root

    if key < root.value:
        root.left = delete_node(root.left, key)
    elif key > root.value:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        temp = min_value_node(root.right)
        root.value = temp.value
        root.right = delete_node(root.right, temp.value)
    return root

def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


# In-order traversal
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=' ')
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print(root.value, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=' ')


# Example usage:
root = Node(10)
root = insert(root, 5)
root = insert(root, 20)
root = insert(root, 3)
root = insert(root, 7)
root = insert(root, 15)
root = insert(root, 30)

print("In-order traversal:")
inorder_traversal(root)
print("\nPre-order traversal:")
preorder_traversal(root)
print("\nPost-order traversal:")
postorder_traversal(root)
