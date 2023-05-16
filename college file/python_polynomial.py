print("\nNAME: Inderpreet Singh\nURN: 2104118\nCRN: 2115064\n")
class Node:
    def __init__(self, coef, exp, next=None):
        self.coef = coef
        self.exp = exp
        self.next = next

class PolyList:
    def __init__(self):
        self.head = Node(0, -1)
        self.head.next = self.head

    def insert(self, coef, exp):
        curr = self.head
        while curr.next != self.head and curr.next.exp > exp:
            curr = curr.next
        if curr.next != self.head and curr.next.exp == exp:
            curr.next.coef += coef
            if curr.next.coef == 0:
                self.delete(curr.next.exp)
        else:
            curr.next = Node(coef, exp, curr.next)

    def delete(self, exp):
        curr = self.head
        while curr.next != self.head and curr.next.exp != exp:
            curr = curr.next
        if curr.next == self.head:
            print("Term not found")
        else:
            curr.next = curr.next.next

    def display(self):
        curr = self.head.next
        while curr != self.head:
            print(curr.coef, "x^", curr.exp, end=' ')
            if curr.next != self.head and curr.next.coef > 0:
                print("+", end=' ')
            curr = curr.next
        print()

def addPoly(poly1, poly2):
    p = PolyList()
    curr1 = poly1.head.next
    curr2 = poly2.head.next
    while curr1 != poly1.head and curr2 != poly2.head:
        if curr1.exp > curr2.exp:
            p.insert(curr1.coef, curr1.exp)
            curr1 = curr1.next
        elif curr1.exp < curr2.exp:
            p.insert(curr2.coef, curr2.exp)
            curr2 = curr2.next
        else:
            p.insert(curr1.coef + curr2.coef, curr1.exp)
            curr1 = curr1.next
            curr2 = curr2.next
    while curr1 != poly1.head:
        p.insert(curr1.coef, curr1.exp)
        curr1 = curr1.next
    while curr2 != poly2.head:
        p.insert(curr2.coef, curr2.exp)
        curr2 = curr2.next
    return p

# Sample usage:
poly1 = PolyList()
poly1.insert(5, 2)
poly1.insert(10, 1)
poly1.insert(6, 0)
print("Poly1:")
poly1.display()

poly2 = PolyList()
poly2.insert(1, 2)
poly2.insert(2, 1)
poly2.insert(4, 0)
print("Poly2:")
poly2.display()

p = addPoly(poly1, poly2)
print("Sum of Poly1 and Poly2:")
p.display()
