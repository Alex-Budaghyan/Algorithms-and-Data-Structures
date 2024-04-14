# from collections import

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insertR(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        elif value < self.root.data:
            if self.root.left is None:
                self.root.left = new_node
            else:
                tmp = BinarySearchTree()
                tmp.root = self.root.left
                tmp.insertR(value)
        elif value > self.root.data:
            if self.root.right is None:
                self.root.right = new_node
            else:
                tmp = BinarySearchTree()
                tmp.root = self.root.right
                tmp.insertR(value)
        else:
            print('skipping data: ', value)

    def insertI(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            parent = None
            runner = self.root
            while runner:
                parent = runner
                if value < runner.data:
                    runner = runner.left
                elif value > runner.data:
                    runner = runner.right
                else:
                    print("skipping data: ", value)
                    return

            if value < parent.data:
                parent.left = new_node
            else:
                parent.right = new_node

    def inorderI(self, node=None):
        if node is None:
            node = self.root
        if node:
            self.inorderI(node.left)
            print(node.data, end=' ')
            self.inorderI(node.right)

    def inorderI(self):
        stack = []
        current = self.root

        while True:
            while current:
                stack.append(current)
                current = current.left

            if len(stack) == 0:
                return

            current = stack[-1]
            stack.pop()
            print(current.data, end=' ')

            current = current.right

    def postorderI(self):
        stack = []
        current = self.root

        while True:
            while current:
                if current.right:
                    stack.append(current.right)
                stack.append(current)
                current = current.left

            if len(stack) == 0:
                return

            current = stack[-1]
            stack.pop()
            if current.right and stack and stack[-1] == current.right:
                stack.pop()
                stack.append(current)
                current = current.right
            else:
                print(current.data, end=' ')
                current = None

    def preorderI(self):
        stack = []
        current = self.root

        while True:
            while current:
                print(current.data, end=' ')
                if current.right:
                    stack.append(current.right)
                current = current.left

            if not stack:
                return

            current = stack[-1]
            stack.pop()

    # def searchI(self, value):
        # current = self.root
        # while current:




if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insertI(20)
    tree.insertR(10)
    tree.insertI(30)
    tree.insertI(10)
    print("Inorder Iterative: ")
    tree.inorderI()
    print("\nPostorder Iterative: ")
    tree.postorderI()
    print("\nPreorder Iterative: ")
    tree.preorderI()
