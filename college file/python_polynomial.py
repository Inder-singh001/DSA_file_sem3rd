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

# class Node:
#     def __init__(self, coeff, expo):
#         self.coefficient = coeff
#         self.exponent = expo
#         self.next = None


# class Polynomial:
#     def __init__(self):
#         self.head = None

#     def add_term(self, coeff, expo):
#         new_node = Node(coeff, expo)
#         if self.head is None:
#             self.head = new_node
#             new_node.next = self.head
#         else:
#             temp = self.head
#             while temp.next != self.head:
#                 temp = temp.next
#             temp.next = new_node
#             new_node.next = self.head

#     def display_polynomial(self, name):
#         temp = self.head
#         poly_string = f"{name}(x, y, z): "
#         while True:
#             coeff_str = ""
#             for i in range(len(temp.coefficient)):
#                 if temp.coefficient[i] != 0:
#                     if i == 0:
#                         coeff_str += f"{temp.coefficient[i]}"
#                     else:
#                         coeff_str += f"{temp.coefficient[i]}{self.get_variable(i)}"
#             if coeff_str != "":
#                 poly_string += f"{coeff_str}{self.get_exponent(temp.exponent)} + "
#             temp = temp.next
#             if temp == self.head:
#                 break
#         poly_string = poly_string.rstrip(" + ")
#         print(poly_string)

#     def get_variable(self, index):
#         variables = ['x', 'y', 'z']
#         return variables[index]

#     def get_exponent(self, exponent):
#         exponent_str = ""
#         for i in range(len(exponent)):
#             if exponent[i] != 0:
#                 exponent_str += f"{self.get_variable(i)}^{exponent[i]}"
#         return exponent_str

#     def add_polynomials(self, poly1, poly2, result_name):
#         temp1 = poly1.head
#         temp2 = poly2.head
#         while True:
#             if temp1.exponent == temp2.exponent:
#                 coeff_sum = [temp1.coefficient[i] + temp2.coefficient[i] for i in range(len(temp1.coefficient))]
#                 self.add_term(coeff_sum, temp1.exponent)
#                 temp1 = temp1.next
#                 temp2 = temp2.next
#             elif temp1.exponent > temp2.exponent:
#                 self.add_term(temp1.coefficient, temp1.exponent)
#                 temp1 = temp1.next
#             else:
#                 self.add_term(temp2.coefficient, temp2.exponent)
#                 temp2 = temp2.next
#             if temp1 == poly1.head or temp2 == poly2.head:
#                 break


# poly1 = Polynomial()
# n = int(input("Enter the number of terms for POLY1: "))
# for _ in range(n):
#     coeff = [int(x) for x in input("Enter the coefficients of POLY1: ").split()]
#     exponent = tuple(int(x) for x in input("Enter the exponents of POLY1: ").split())
#     poly1.add_term(coeff, exponent)

# poly2 = Polynomial()
# n = int(input("Enter the number of terms for POLY2: "))
# for _ in range(n):
#     coeff = [int(x) for x in input("Enter the coefficients of POLY2: ").split()]
#     exponent = tuple(int(x) for x in input("Enter the exponents of POLY2: ").split())
#     poly2.add_term(coeff, exponent)

# poly_sum = Polynomial()
# poly_sum.add_polynomials(poly1, poly2, "POLYSUM")

# poly1.display_polynomial("POLY1")
# poly2.display_polynomial("POLY2")
# poly_sum.display_polynomial("POLYSUM")
