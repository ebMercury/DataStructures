class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Binarytree:
    def __init__(self):
        self.stack = []

    def inorder(self, root):
        r = root
        while True:
            if r is not None:
                self.stack.append(r)
                r = r.left
            elif self.stack:
                r = self.stack.pop()
                print(r.data, end=' ')
                r = r.right
            else:
                break

    def postorder(self, root):
        pass

r = Node(1,
         left=Node(2,
                   left=Node(4),
                   right=Node(5)
                   ),
         right=Node(3)
         )

b = Binarytree()
print(b.inorder(r))
