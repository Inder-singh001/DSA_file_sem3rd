print("\nNAME: Inderpreet Singh\nURN: 2104118\nCRN: 2115064\n")

class Student:
    def __init__(self):
        self.urn = ""
        self.name = ""
        self.branch = ""
        self.sem = ""
        self.phno = ""
        self.next = None

class StudentLinkedList:
    def __init__(self):
        self.head = None
    
    # Function to insert a student at the front of the linked list
    def front_insert(self):
        student = Student()
        student.urn = input("Enter URN: ")
        student.name = input("Enter Name: ")
        student.branch = input("Enter Branch: ")
        student.sem = input("Enter Sem: ")
        student.phno = input("Enter PhNo: ")
        student.next = self.head
        self.head = student
        print("Student inserted successfully!")
    
    # Function to display the status of the linked list and count the number of nodes
    def display(self):
        count = 0
        print("URN\tName\tBranch\tSem\tPhNo")
        current = self.head
        while current:
            print(current.urn, "\t", current.name, "\t", current.branch, "\t", current.sem, "\t", current.phno)
            count += 1
            current = current.next
        print("Number of students: ", count)
    
    # Function to insert a student at the end of the linked list
    def end_insert(self):
        student = Student()
        student.urn = input("Enter URN: ")
        student.name = input("Enter Name: ")
        student.branch = input("Enter Branch: ")
        student.sem = input("Enter Sem: ")
        student.phno = input("Enter PhNo: ")
        if self.head is None:
            self.head = student
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = student
        print("Student inserted successfully!")
    
    # Function to delete a student from the end of the linked list
    def end_delete(self):
        if self.head is None:
            print("List is empty!")
        elif self.head.next is None:
            self.head = None
            print("Student deleted successfully!")
        else:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None
            print("Student deleted successfully!")
    
    # Function to insert a student at the front of the linked list (demonstration of stack)
    def push(self):
        self.front_insert()
    
    # Function to delete a student from the front of the linked list (demonstration of stack)
    def pop(self):
        if self.head is None:
            print("List is empty!")
        else:
            self.head = self.head.next
            print("Student deleted successfully!")
    
    # Function to display the menu and handle user inputs
    def menu(self):
        while True:
            print("\nMENU____\n")
            print("1. Insert at front")
            print("2. Display list")
            print("3. Insert at end")
            print("4. Delete from end")
            print("5. Push (Insert at front - stack demonstration)")
            print("6. Pop (Delete from front - stack demonstration)")
            print("7. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.front_insert()
            elif choice == 2:
                self.display()
            elif choice == 3:
                self.end_insert()
            elif choice == 4:
                self.end_delete()
            elif choice == 5:
                self.push()
            elif choice == 6:
                self.pop()
            elif choice == 7:
                print("Exiting the program.....")
                break;
            else:
                print("Invalid choice")

if __name__ == '__main__':
    sll = StudentLinkedList()
    sll.menu()
