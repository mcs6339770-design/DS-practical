class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree(expression):
    stack = []

    for ch in expression:

        if ch.isalnum():
            stack.append(Node(ch))

        else:
            node = Node(ch)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)

    return stack[-1]


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


expression = input("Enter postfix expression: ")

root = build_tree(expression)

print("Inorder:")
inorder(root)

print("\nPreorder:")
preorder(root)

print("\nPostorder:")
postorder(root)