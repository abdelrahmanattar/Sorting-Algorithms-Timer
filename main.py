import random
import time


def selection_sort(arr, n):
    for i in range(n):
        iMin = i
        for j in range(i + 1, n):
            if arr[j] < arr[iMin]:
                iMin = j
        if i != iMin:
            arr[i], arr[iMin] = arr[iMin], arr[i]


def bubble_sort(arr, n):
    for i in range(1, n):
        flag = 0
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = 1
        if flag == 0:
            break


def insertion_sort(arr, n):
    for i in range(1, n):
        key = arr[i]
        hole = i
        while (hole > 0) & (arr[hole - 1] > key):
            arr[hole] = arr[hole - 1]
            hole = hole - 1
        arr[hole] = key


def merge(left, right, arr):
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


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(left, right, arr)


def partition(arr, first, last):
    index = random.randint(first, last)
    pivot = arr[index]
    arr[index], arr[last] = arr[last], arr[index]
    lower = (first - 1)
    for current in range(first, last):
        if arr[current] <= pivot:
            lower += 1
            arr[lower], arr[current] = arr[current], arr[lower]
    arr[lower + 1], arr[last] = arr[last], arr[lower + 1]
    return lower + 1


def quick_sort(arr, first, last):
    if first < last:
        part = partition(arr, first, last)
        quick_sort(arr, first, part - 1)
        quick_sort(arr, part + 1, last)


def hybrid_sort(arr, threshold):
    if len(arr) > threshold:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        hybrid_sort(left, threshold)
        hybrid_sort(right, threshold)
        merge(left, right, arr)
    else:
        selection_sort(arr, len(arr))


def find_kth_element(arr, first, last, smallest):
    if first <= last:
        key = partition(arr, first, last)
        if key == smallest:
            return arr[key]
        if key > smallest:
            return find_kth_element(arr, first, key - 1, smallest)
        if key < smallest:
            return find_kth_element(arr, key + 1, last, smallest)


def time_calculator(arr, sort_type):
    match sort_type:
        case 0:
            begin = time.time()
            merge_sort(arr)
            time.sleep(1)
            end = time.time()
            return end - begin
        case 1:
            begin = time.time()
            quick_sort(arr, 0, len(arr) - 1)
            time.sleep(1)
            end = time.time()
            return end - begin
        case 2:
            begin = time.time()
            insertion_sort(arr, len(arr))
            time.sleep(1)
            end = time.time()
            return end - begin
        case 3:
            begin = time.time()
            selection_sort(arr, len(arr))
            time.sleep(1)
            end = time.time()
            return end - begin
        case 4:
            begin = time.time()
            bubble_sort(arr, len(arr))
            time.sleep(1)
            end = time.time()
            return end - begin
        case 5:
            begin = time.time()
            hybrid_sort(arr, threshold)
            time.sleep(1)
            end = time.time()
            return end - begin
        case 6:
            return find_kth_element(arr, 0, len(arr)-1, number - 1)


# MAIN INTERFACE
print(
    "                                                            ************ WELCOME TO OUR SORTING SYSTEM TIMER ************")
print("-- please enter the size of the array you want to sort --"
      "")
size_array = int(input())
print("please enter the hybrid sorting threshold"
      "")
threshold = int(input())
A = [random.randrange(1, 1000, 1) for i in range(size_array)]
B = [A[i] for i in range(len(A))]
print("merge sort time: " + str(time_calculator(B, 0)) + "secs")
B = [A[i] for i in range(len(A))]
print("quick sort time " + str(time_calculator(B, 1)) + "secs")
B = [A[i] for i in range(len(A))]
print("insertion sort time: " + str(time_calculator(B, 2)) + "secs")
B = [A[i] for i in range(len(A))]
print("selection sort time: " + str(time_calculator(B, 3)) + "secs")
B = [A[i] for i in range(len(A))]
print("bubble sort time: " + str(time_calculator(B, 4)) + "secs")
B = [A[i] for i in range(len(A))]
print("Hybrid sort time: " + str(time_calculator(B, 5)) + "secs")
B = [A[i] for i in range(len(A))]
runner = True
while runner:
    print("please choose which function you want to work with")
    print("1.Merge Sort        2.Quick Sort")
    print("3.Insertion Sort    4.Selection Sort")
    print("5.Bubble Sort       6.Hybrid Sort")
    print("7.Find k(th) Element")
    print("** Note ** Find k(th) element won't return the time of sorting technique it is the only function returns an element"
          "")
    choice = int(input()) - 1
    if choice == 6:
        print("please enter the kth number to search for")
        number = int(input())
        print("Element no." + str(number) + ": " + str(time_calculator(B, choice)))
    else:
        print("time taken: " + str(time_calculator(B, 5)) + "secs")

    print("if you want to exit enter 'Yes' ")
    variable = input().lower()
    if variable == "yes":
        runner = False
