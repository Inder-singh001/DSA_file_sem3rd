# Function to create an array of N integer elements
def create_array(n):
    arr = []
    for i in range(n):
        elem = int(input(f"Enter element {i+1}: "))
        arr.append(elem)
    return arr

# Function to display array elements with suitable headings
def display_array(arr):
    print("Array Elements:")
    for i in range(len(arr)):
        print(f"Element {i+1}: {arr[i]}")

# Function to insert an element (elem) at a given valid position (pos)
def insert_element(arr, elem, pos):
    arr.insert(pos-1, elem)
    return arr

# Function to delete an element at a given valid position (pos)
def delete_element(arr, pos):
    del arr[pos-1]
    return arr

# Main program
arr = []
while True:
    print("\nArray Operations Menu")
    print("1. Create Array")
    print("2. Display Array")
    print("3. Insert Element")
    print("4. Delete Element")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter the number of elements: "))
        arr = create_array(n)
    elif choice == 2:
        if len(arr) == 0:
            print("Array is empty. Please create an array first.")
        else:
            display_array(arr)
    elif choice == 3:
        if len(arr) == 0:
            print("Array is empty. Please create an array first.")
        else:
            elem = int(input("Enter the element to be inserted: "))
            pos = int(input("Enter the position at which to insert the element: "))
            arr = insert_element(arr, elem, pos)
            print("Element inserted successfully.")
    elif choice == 4:
        if len(arr) == 0:
            print("Array is empty. Please create an array first.")
        else:
            pos = int(input("Enter the position of the element to be deleted: "))
            arr = delete_element(arr, pos)
            print("Element deleted successfully.")
    elif choice == 5:
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter a valid choice.")
        
print("\n\nName : Inderpreet Singh\n URN : 2104118")