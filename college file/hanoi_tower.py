print("\nNAME: Inderpreet Singh\nURN: 2104118\nCRN: 2115064\n")
import operator

# dictionary to store operator functions
ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '%': operator.mod, '^': operator.pow}

# function to evaluate suffix expression
def evaluate_suffix_expression(expression):
    stack = []
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            result = ops[char](a, b)
            stack.append(result)
    return stack.pop()

# example usage
expression = input("Enter suffix expression: ")
result = evaluate_suffix_expression(expression)
print(f"{expression} = {result}")

# function to solve Tower of Hanoi problem
def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n-1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n-1, auxiliary, destination, source)

# example usage
n = 3
tower_of_hanoi(n, 'A', 'C', 'B')
