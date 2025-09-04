# Binary Search Tree implementation

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.key:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def inorder(self, root):
        return self.inorder(root.left) + [root.key] + self.inorder(root.right) if root else []

    def preorder(self, root):
        return [root.key] + self.preorder(root.left) + self.preorder(root.right) if root else []

    def postorder(self, root):
        return self.postorder(root.left) + self.postorder(root.right) + [root.key] if root else []


if __name__ == "__main__":
    bt = BinaryTree()
    for val in [10, 30, 25, 9, 8, 40, 4, 50]:
        bt.insert(val)

    print("Inorder:", bt.inorder(bt.root))
    print("Preorder:", bt.preorder(bt.root))
    print("Postorder:", bt.postorder(bt.root))
