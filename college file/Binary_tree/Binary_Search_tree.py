print("\nNAME: Inderpreet Singh\nURN: 2104118\nCRN: 2115064\n")

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(node.right, data)

    def inorder_traversal(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if node:
            self._inorder_recursive(node.left)
            print(node.data, end=" ")
            self._inorder_recursive(node.right)

    def preorder_traversal(self):
        self._preorder_recursive(self.root)

    def _preorder_recursive(self, node):
        if node:
            print(node.data, end=" ")
            self._preorder_recursive(node.left)
            self._preorder_recursive(node.right)

    def postorder_traversal(self):
        self._postorder_recursive(self.root)

    def _postorder_recursive(self, node):
        if node:
            self._postorder_recursive(node.left)
            self._postorder_recursive(node.right)
            print(node.data, end=" ")

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.data == key:
            return node
        if key < node.data:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

# Main program
bst = BST()

# Create a BST of N Integers
data_list = [6, 9, 5, 2, 8, 15, 24, 14, 7, 8, 5, 2]
for data in data_list:
    bst.insert(data)

while True:
    print("\n----- Binary Search Tree (BST) Menu -----")
    print("1. Traverse the BST in Inorder")
    print("2. Traverse the BST in Preorder")
    print("3. Traverse the BST in Postorder")
    print("4. Search the BST for a given element")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("Inorder Traversal: ", end="")
        bst.inorder_traversal()
    elif choice == '2':
        print("Preorder Traversal: ", end="")
        bst.preorder_traversal()
    elif choice == '3':
        print("Postorder Traversal: ", end="")
        bst.postorder_traversal()
    elif choice == '4':
        key = int(input("Enter the element to search: "))
        result = bst.search(key)
        if result:
            print("Element", key, "found in the BST.")
        else:
            print("Element", key, "not found in the BST.")
    elif choice == '5':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
