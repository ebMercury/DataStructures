class Node:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_data(self):
        return self.data


class BinaryTree:
    def __init__(self):
        self.x = []
        self.count = 0

    def inorder(self, root):
        if root:
            self.inorder(root.get_left())
            self.x.append(root.get_data())
            self.inorder(root.get_right())
        return self.x

    def number_of_nodes(self, root):
        ln = 0
        rn = 0
        if root.get_left():
            ln = self.number_of_nodes(root.get_left())
        if root.get_right():
            rn = self.number_of_nodes(root.get_right())
        return ln + rn + 1

    def is_full(self, root):
        c = root
        if c is None:
            return True
        if c.left is None and c.right is None:
            return True

        if c.left is not None and c.right is not None:
            return self.is_full(c.left) and self.is_full(c.right)

        return False

    def is_complete(self, root):
        pass

    def height(self, root):
        if root is None:
            return 0
        else:
            lheight = self.height(root.left)
            rheight = self.height(root.left)
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1

    def print_level_order(self, root):
        h = self.height(root)
        for i in range(1, h + 1):
            self.print_current_level(root, i)

    def print_current_level(self, root, level):
        if root is None:
            return
        if level == 1:
            print(root.data, end=" ")
        elif level > 1:
            self.print_current_level(root.left, level - 1)
            self.print_current_level(root.right, level - 1)

    def degree(self, root):
        c = root

        if c.left is not None and c.right is not None:
            self.count += 1

            return self.degree(c.left) and self.degree(c.right)


r = Node(1,
         left=Node(2,
                   left=Node(4),
                   right=Node(5)
                   ),
         right=Node(3,
                    left=Node(6),
                    right=Node(7,
                               left=Node(8),
                               right=Node(9))
                    )
         )

b = BinaryTree()
b.degree(r)
print(b.count)
