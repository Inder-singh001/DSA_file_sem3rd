
top = -1
stack = []

# create a stack
def my_stack(n):
    stack=[]
    for i in range(n):
        elem = int(input(f"Enter element {i+1}: "))
        stack.append(elem)
    return stack

# push elements into stack
def push_element(stack, elem):
    global top
    top += 1
    stack.append(elem)
    return stack

# pop element from stack
def pop_element(stack):
    global top
    if top == -1:
        print("\nEmpty stack. First, create a stack")
        return stack
    else:
        print("\n",stack.pop(-1),"\n")
        top -= 1
        return stack

# check if string is palindrome
def is_palindrome(string):
    global top
    for char in string:
        push_element(stack, ord(char))
    reversed_string = ""
    while top != -1:
        reversed_string += chr(stack[top])
        pop_element(stack)
    if string == reversed_string:
        print(f"{string} is a palindrome")
    else:
        print(f"{string} is not a palindrome")


while True:
    print("\nStack Operations")
    print("1. Create Stack")
    print("2. Push the element")
    print("3. Pop the element")
    print("4. To check if the stack is palindrome")
    print("5. Exit the program")
    choice = int(input("\nEnter your choice: "))
    
    if choice==1:
        n = int(input("\nEnter the number of elements: "))
        stack = my_stack(n)
        top = len(stack) - 1
        print("\nSTACK= ",stack)
    elif choice==2:
        if len(stack)==0:
            print("\nEmpty stack. First, create a stack") 
        else:
            elem = int(input("Enter the element to be inserted: "))
            stack = push_element(stack, elem)
            print("Element inserted successfully.")
            print("\nSTACK= ",stack)             
    elif choice==3:
        stack = pop_element(stack)
        print("\nSTACK= ",stack)
        print("Select option-3, to pop another element from stack.\n")
    elif choice == 4:
            string = input("Enter string to check palindrome: ")
            is_palindrome(string)
    elif choice==5: 
        print("Exiting the program....\n")
        break
    else:
        print("Invalid Choice.")
