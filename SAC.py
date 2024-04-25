import random
import time
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
def compare_performance():
    arr = random.sample(range(1, 100000), 10000)
    start_time = time.time()
    bubble_sort(arr)
    bubble_sort_time = time.time() - start_time
    start_time = time.time()
    sorted(arr)
    sorted_time = time.time() - start_time
    print(f"Time taken by Bubble Sort: {bubble_sort_time} seconds")
    print(f"Time taken by sorted() function: {sorted_time} seconds")
compare_performance()