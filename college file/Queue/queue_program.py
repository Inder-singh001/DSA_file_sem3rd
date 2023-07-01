print("\nNAME: Inderpreet Singh\nURN: 2104118\nCRN: 2115064\n")
MAX = 5
queue = [''] * MAX
front = -1
rear = -1

# Function to insert an element onto the Circular Queue
def insert():
    global front, rear
    if ((front == 0 and rear == MAX-1) or (front == rear+1)):
        print("Circular Queue Overflow!")
    else:
        char = input("Enter a character to insert: ")
        if (front == -1):
            front = 0
            rear = 0
        elif (rear == MAX-1):
            rear = 0
        else:
            rear += 1
        queue[rear] = char
        print(char, "has been inserted into the Circular Queue.")
        
# Function to delete an element from the Circular Queue
def delete():
    global front, rear
    if (front == -1):
        print("Circular Queue Underflow!")
    else:
        char = queue[front]
        if (front == rear):
            front = -1
            rear = -1
        elif (front == MAX-1):
            front = 0
        else:
            front += 1
        print(char, "has been deleted from the Circular Queue.")

# Function to display the status of the Circular Queue
def display():
    global front, rear
    if (front == -1):
        print("Circular Queue is Empty!")
    else:
        print("Front ->", end=" ")
        for i in range(front, rear+1):
            print(queue[i], end=" ")
        print("<- Rear")

# Main program loop
while True:
    print("\nMENU\n----")
    print("1. Insert an element onto the Circular Queue")
    print("2. Delete an element from the Circular Queue")
    print("3. Demonstrate Overflow and Underflow situations on Circular Queue")
    print("4. Display the status of the Circular Queue")
    print("5. Exit")
    choice = int(input("Enter your choice (1-5): "))
    if choice == 1:
        insert()
    elif choice == 2:
        delete()
    elif choice == 3:
        # Demonstrate Overflow and Underflow situations
        for i in range(MAX+1):
            insert()
        for i in range(MAX+1):
            delete()
    elif choice == 4:
        display()
    elif choice == 5:
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice! Please choose again.")
