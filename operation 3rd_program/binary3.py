class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_operator(value):
    return value in "+-*/"


def construct_expression_tree(expression):
    stack = []

    for item in expression.split():

        if not is_operator(item):
            stack.append(Node(item))

        else:
            node = Node(item)

            node.right = stack.pop()
            node.left = stack.pop()

            stack.append(node)

    return stack.pop()


def evaluate(root):
    if root.left is None and root.right is None:
        return float(root.value)

    left = evaluate(root.left)
    right = evaluate(root.right)

    if root.value == '+':
        return left + right
    elif root.value == '-':
        return left - right
    elif root.value == '*':
        return left * right
    elif root.value == '/':
        return left / right


expression = input("Enter postfix expression: ")

root = construct_expression_tree(expression)

print("Expression Tree Evaluated Result:", evaluate(root))