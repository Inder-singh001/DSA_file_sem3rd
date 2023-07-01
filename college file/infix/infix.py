
import string

# function to check if a character is an operand
def is_operand(c):
    return c.isalnum()

# function to check the precedence of operators
def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/' or operator == '%':
        return 2
    elif operator == '^':
        return 3
    else:
        return 0

# function to convert infix expression to postfix expression
def infix_to_postfix(infix):
    stack = []
    postfix = ""
    for i in infix:
        if is_operand(i):
            postfix += i
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        else:
            while stack and precedence(i) <= precedence(stack[-1]):
                postfix += stack.pop()
            stack.append(i)
    while stack:
        postfix += stack.pop()
    return postfix

# main program
infix = input("Enter an infix expression: ")
postfix = infix_to_postfix(infix)
print("Postfix expression:", postfix)
