
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


expression = input("Enter suffix expression: ")
result = evaluate_suffix_expression(expression)
print(f"{expression} = {result}")

def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return [f"Move disk 1 from {source} to {destination}"]

    moves = []
    moves.extend(tower_of_hanoi(n - 1, source, auxiliary, destination))
    print(f"Move disk {n} from {source} to {destination}")
    moves.extend(tower_of_hanoi(n - 1, auxiliary, destination, source))

    return moves

n = (int(input("Enter the number of disks: ")))
source = input("Enter the name of the source rod: ")
auxiliary = input("Enter the name of the auxiliary rod: ")
destination = input("Enter the name of the destination rod: ")
moves = tower_of_hanoi(n, source, auxiliary, destination)
