# =========================================================
# UNIT 3 ASSIGNMENT - SORTING ALGORITHMS
# Insertion Sort, Merge Sort, Quick Sort
# Dataset Benchmarking and Analysis
# =========================================================

import random
import time

# =========================================================
# INSERTION SORT
# =========================================================

def insertion_sort(arr):
    a = arr.copy()

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a


# =========================================================
# MERGE SORT
# =========================================================

def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# =========================================================
# QUICK SORT
# =========================================================

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = []
    right = []

    for x in arr[:-1]:

        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    return quick_sort(left) + [pivot] + quick_sort(right)


# =========================================================
# DATASET GENERATION
# =========================================================

def generate_random_data(size):
    return [random.randint(1, 100000) for _ in range(size)]


def generate_sorted_data(size):
    return list(range(size))


def generate_reverse_data(size):
    return list(range(size, 0, -1))


# =========================================================
# TIME MEASUREMENT FUNCTION
# =========================================================

def measure_time(sort_function, data):

    start = time.time()

    sort_function(data)

    end = time.time()

    return round(end - start, 6)


# =========================================================
# BENCHMARKING
# =========================================================

sizes = [1000, 5000, 10000]

print("\n================ BENCHMARK RESULTS ================\n")

for size in sizes:

    print(f"\nDATASET SIZE : {size}")
    print("-" * 60)

    datasets = {
        "Random": generate_random_data(size),
        "Sorted": generate_sorted_data(size),
        "Reverse": generate_reverse_data(size)
    }

    for dataset_name, data in datasets.items():

        print(f"\n{dataset_name} Data:")

        insertion_time = measure_time(insertion_sort, data.copy())
        merge_time = measure_time(merge_sort, data.copy())
        quick_time = measure_time(quick_sort, data.copy())

        print(f"Insertion Sort Time : {insertion_time} seconds")
        print(f"Merge Sort Time     : {merge_time} seconds")
        print(f"Quick Sort Time     : {quick_time} seconds")


# =========================================================
# SAMPLE TEST
# =========================================================

sample = [64, 34, 25, 12, 22, 11, 90]

print("\n================ SAMPLE SORTING =================")

print("\nOriginal Array:")
print(sample)

print("\nInsertion Sort:")
print(insertion_sort(sample))

print("\nMerge Sort:")
print(merge_sort(sample))

print("\nQuick Sort:")
print(quick_sort(sample))


# =========================================================
# THEORY NOTES
# =========================================================

print("\n================ THEORY NOTES =================")

print("""
1. Insertion Sort
   - Best Case  : O(n)
   - Worst Case : O(n^2)
   - Stable     : Yes
   - In-place   : Yes

2. Merge Sort
   - Best Case  : O(n log n)
   - Worst Case : O(n log n)
   - Stable     : Yes
   - In-place   : No
   - Uses extra memory during merging.

3. Quick Sort
   - Average Case : O(n log n)
   - Worst Case   : O(n^2)
   - Stable       : No
   - In-place     : Depends on implementation

Worst case in Quick Sort occurs when:
- Pivot selection is poor
- Example: already sorted array with last element as pivot
""")