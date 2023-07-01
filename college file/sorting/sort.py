print("\nNAME: Inderpreet Singh\nURN: 2104118\nCRN: 2115064\n")

import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_value = max(arr)
    exp = 1
    while max_value // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
        
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def quick_sort(arr):
    _quick_sort(arr, 0, len(arr) - 1)

def _quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        _quick_sort(arr, low, pi - 1)
        _quick_sort(arr, pi + 1, high)
        
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Function to generate a random list of given size
def generate_random_list(size):
    return [random.randint(1, 100) for _ in range(size)]

# Function to measure the execution time of a sorting algorithm
def measure_execution_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time

# Function to compare the performance of different sorting algorithms
def compare_sorting_algorithms(size):
    arr = generate_random_list(size)

    bubble_time = measure_execution_time(bubble_sort, arr.copy())
    selection_time = measure_execution_time(selection_sort, arr.copy())
    insertion_time = measure_execution_time(insertion_sort, arr.copy())
    radix_time = measure_execution_time(radix_sort, arr.copy())
    merge_time = measure_execution_time(merge_sort, arr.copy())
    quick_time = measure_execution_time(quick_sort, arr.copy())

    print("Size of the list:", size)
    print("Bubble Sort Time:", bubble_time)
    print("Selection Sort Time:", selection_time)
    print("Insertion Sort Time:", insertion_time)
    print("Radix Sort Time:", radix_time)
    print("Merge Sort Time:", merge_time)
    print("Quick Sort Time:", quick_time)

# Main program
size = int(input("Enter the size of the list: "))
compare_sorting_algorithms(size)

