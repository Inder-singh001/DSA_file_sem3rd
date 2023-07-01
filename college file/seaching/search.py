print("\nNAME: Inderpreet Singh\nURN: 2104118\nCRN: 2115064\n")

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Main program
arr = list(map(int, input("Enter the elements of the array (space-separated): ").split()))
target = int(input("Enter the element to search: "))

linear_result = linear_search(arr, target)
binary_result = binary_search(arr, target)

if linear_result != -1:
    print("Linear Search: Element found at position", linear_result + 1)
else:
    print("Linear Search: Element not found")

if binary_result != -1:
    print("Binary Search: Element found at position", binary_result + 1)
else:
    print("Binary Search: Element not found")
