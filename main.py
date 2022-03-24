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
    index = random.randrange(0,last, 1)
    pivot = arr[index]
    arr[last - 1], arr[index] = arr[index], arr[last - 1]
    i = -1
    for j in range(first + 1, last):
        if arr[j] <= pivot:
            index = index + 1
            arr[index], arr[j] = arr[j], arr[index]
        arr[index + 1] = arr[last]
    return index + 1


def quick_sort(arr, first, last):
    if first < last:
        part_index = partition(arr, first, last)
        quick_sort(arr, first, part_index - 1)
        quick_sort(arr, part_index + 1, last)


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


# MAIN INTERFACE
print("                                                            ************ WELCOME TO OUR SORTING SYSTEM TIMER ************")
print("-- please enter the size of the array you want to sort --"
      "")
size_array = int(input())
print("please enter the hybrid sorting threshold"
      "")
threshold = int(input())
A = [random.randrange(1, 1000, 1) for i in range(size_array)]
B = [A[i] for i in range(len(A))]
begin = time.time()
merge_sort(B)
time.sleep(1)
end = time.time()
time_of_sorting = str(end - begin)
print("merge sort time: " + time_of_sorting + " secs")
B = [A[i] for i in range(len(A))]
begin = time.time()
insertion_sort(B, len(B))
time.sleep(1)
end = time.time()
time_of_sorting = str(end - begin)
print("insertion sort time: " + time_of_sorting + " secs")
B = [A[i] for i in range(len(A))]
begin = time.time()
selection_sort(B, len(B))
time.sleep(1)
end = time.time()
time_of_sorting = str(end - begin)
print("selection sort time: " + time_of_sorting + " secs")
B = [A[i] for i in range(len(A))]
begin = time.time()
hybrid_sort(B, threshold)
time.sleep(1)
end = time.time()
time_of_sorting = str(end - begin)
print("hybrid sort time: " + time_of_sorting + " secs")
