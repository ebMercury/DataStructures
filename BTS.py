class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


def insert(root, k):
    if root is None:
        return Node(k)
    elif k < root.key:
        root.left = insert(root.left, k)
    else:
        root.right = insert(root.right, k)
    return root


def search(root, k):
    if root is None or root.key == k:
        return root
    if k > root.key:
        return search(root.right, k)
    return search(root.left, k)


def deleteNode(root, k):
    # Base case
    if root is None:
        return root

    # Recursive calls for ancestors of
    # node to be deleted
    if root.key > k:
        root.left = deleteNode(root.left, k)
        return root
    elif root.key < k:
        root.right = deleteNode(root.right, k)
        return root

    # We reach here when root is the node
    # to be deleted.

    # If one of the children is empty
    if root.left is None:
        temp = root.right
        del root
        return temp
    elif root.right is None:
        temp = root.left
        del root
        return temp

    # If both children exist
    else:

        succParent = root

        # Find successor
        succ = root.right
        while succ.left is not None:
            succParent = succ
            succ = succ.left

        # Delete successor.  Since successor
        # is always left child of its parent
        # we can safely make successor's right
        # right child as left of its parent.
        # If there is no succ, then assign
        # succ.right to succParent.right
        if succParent != root:
            succParent.left = succ.right
        else:
            succParent.right = succ.right

        # Copy Successor Data to root
        root.key = succ.key

        # Delete Successor and return root
        del succ
        return root


def min_value_node(root):
    c = root
    while c.left is not None:
        c = c.left
    return c


def max_value_node(root):
    c = root
    while c.right is not None:
        c = c.right
    return c


r = None
r = insert(r, 4)
r = insert(r, 2)
r = insert(r, 3)
r = insert(r, 6)
r = insert(r, 5)
r = insert(r, 7)
r = insert(r, 1)
r = insert(r, 16)

mini = min_value_node(r)
maxi = max_value_node(r)
print(mini.key, maxi.key)
