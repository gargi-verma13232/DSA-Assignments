# ==============================
# 1. FACTORIAL (RECURSIVE)
# ==============================
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# ==============================
# 2. FIBONACCI (NAIVE)
# ==============================
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


# ==============================
# 3. FIBONACCI (MEMOIZATION)
# ==============================
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


# ==============================
# 4. TOWER OF HANOI
# ==============================
def tower_of_hanoi(n, source, helper, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    tower_of_hanoi(n - 1, source, destination, helper)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, helper, source, destination)


# ==============================
# 5. RECURSIVE BINARY SEARCH
# ==============================
def binary_search(arr, left, right, target):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, left, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, right, target)


# ==============================
# MAIN DEMONSTRATION (IMPORTANT)
# ==============================
if __name__ == "__main__":

    print("---- Factorial ----")
    print("Factorial of 5:", factorial(5))

    print("\n---- Fibonacci (Naive) ----")
    print("Fib(6):", fib_naive(6))

    print("\n---- Fibonacci (Memoized) ----")
    print("Fib(6):", fib_memo(6))

    print("\n---- Tower of Hanoi (N=3) ----")
    tower_of_hanoi(3, 'A', 'B', 'C')

    print("\n---- Binary Search ----")
    arr = [1, 3, 5, 7, 9, 11]
    target = 7
    result = binary_search(arr, 0, len(arr) - 1, target)

    if result != -1:
        print(f"Element {target} found at index:", result)
    else:
        print("Element not found")