
class Employee:
    def __init__(self, ssn, name, dept, designation, sal, phno):
        self.ssn = ssn
        self.name = name
        self.dept = dept
        self.designation = designation
        self.sal = sal
        self.phno = phno
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertEnd(self, employee):
        if self.head is None:
            self.head = employee
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = employee
            employee.prev = current

    def displayStatus(self):
        if self.head is None:
            print("DLL is empty.")
        else:
            current = self.head
            while current:
                print("SSN:", current.ssn)
                print("Name:", current.name)
                print("Dept:", current.dept)
                print("Designation:", current.designation)
                print("Salary:", current.sal)
                print("Phone Number:", current.phno)
                print("---------------------------")
                current = current.next

    def countNodes(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def insertEndDLL(self):
        ssn = input("Enter SSN: ")
        name = input("Enter Name: ")
        dept = input("Enter Dept: ")
        designation = input("Enter Designation: ")
        sal = float(input("Enter Salary: "))
        phno = input("Enter Phone Number: ")
        employee = Employee(ssn, name, dept, designation, sal, phno)
        self.insertEnd(employee)
        print("Employee data inserted at the end of DLL.")

    def deleteEndDLL(self):
        if self.head is None:
            print("DLL is empty.")
        else:
            current = self.head
            prev = None
            while current.next:
                prev = current
                current = current.next
            if prev:
                prev.next = None
            else:
                self.head = None
            print("Employee data deleted from the end of DLL.")

    def insertFrontDLL(self):
        ssn = input("Enter SSN: ")
        name = input("Enter Name: ")
        dept = input("Enter Dept: ")
        designation = input("Enter Designation: ")
        sal = float(input("Enter Salary: "))
        phno = input("Enter Phone Number: ")
        employee = Employee(ssn, name, dept, designation, sal, phno)
        if self.head is None:
            self.head = employee
        else:
            employee.next = self.head
            self.head.prev = employee
            self.head = employee
        print("Employee data inserted at the front of DLL.")

    def deleteFrontDLL(self):
        if self.head is None:
            print("DLL is empty.")
        else:
            temp = self.head
            self.head = temp.next
            if self.head:
                self.head.prev = None
            print("Employee data deleted from the front of DLL.")

    def useAsDeque(self):
        while True:
            print("\n----- Double Ended Queue Menu -----")
            print("1. Insert at Front")
            print("2. Delete from Front")
            print("3. Insert at End")
            print("4. Delete from End")
            print("5. Display Status")
            print("6. Exit Double Ended Queue")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.insertFrontDLL()
            elif choice == '2':
                self.deleteFrontDLL()
            elif choice == '3':
                self.insertEndDLL()
            elif choice == '4':
                self.deleteEndDLL()
            elif choice == '5':
                self.displayStatus()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

# Main program
dll = DoublyLinkedList()

while True:
    print("\n----- Doubly Linked List (DLL) Menu -----")
    print("1. Create a DLL of N Employees Data")
    print("2. Display the status of DLL and count the number of nodes")
    print("3. Perform Insertion at End of DLL")
    print("4. Perform Deletion at End of DLL")
    print("5. Perform Insertion at Front of DLL")
    print("6. Perform Deletion at Front of DLL")
    print("7. Use DLL as Double Ended Queue")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        n = int(input("Enter the number of employees: "))
        for _ in range(n):
            dll.insertEndDLL()
        print("DLL of N Employees created successfully.")
    elif choice == '2':
        dll.displayStatus()
        count = dll.countNodes()
        print("Number of nodes in DLL:", count)
    elif choice == '3':
        dll.insertEndDLL()
    elif choice == '4':
        dll.deleteEndDLL()
    elif choice == '5':
        dll.insertFrontDLL()
    elif choice == '6':
        dll.deleteFrontDLL()
    elif choice == '7':
        dll.useAsDeque()
    elif choice == '8':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")

