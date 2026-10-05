def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3
    return 0


def infix_to_postfix(expression):
    stack = []
    result = ""

    for ch in expression:

        if ch.isalnum():
            result += ch

        elif ch == '(':
            stack.append(ch)

        elif ch == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()

        else:
            while (stack and stack[-1] != '(' and
                   precedence(stack[-1]) >= precedence(ch)):
                result += stack.pop()

            stack.append(ch)

    while stack:
        result += stack.pop()

    return result


expression = input("Enter infix expression: ")

print("Postfix expression:", infix_to_postfix(expression))