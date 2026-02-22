# Experiment 4 :
    #   Fibonacci (Naive vs Memoized) + Call Counter
# Aim :
    #   Understand inefficiency of naive recursion and benefit of memoization.
# What you will implement (in lab) :
    #   Implement fib naive(n) and fib memo(n) with call counters. Compare call counts for
    #n=10,20,30 to show performance difference clearly.
# Input / Output expectation :
    #Input: n values. Output: fib(n) + calls naive + calls memo + short explanation (3–4
    #lines).
# Lab checkpoints (faculty verifies) :
    #• Memoized version drastically reduces calls
    #• Student can explain repeated subproblems
# Viva :
    #1. Why naive Fibonacci is slow?
    #2. Memoization relates to DP ?
    #3. Space impact of memoization?


# SOLUTION :
# This program compares naive recursion and memoization
# by counting how many times the function is called.

# Complexity Explanation:
# Naive Version:
# Time Complexity ≈ O(2^n) because same values are calculated again and again.
# Memoized Version:
# Time Complexity = O(n) because each value is calculated only once and stored.
# Space Complexity = O(n) (due to recursion stack + storage)



# Naive Fibonacci
naive_calls = 0  # counter for naive calls
def fib_naive(n):
    global naive_calls
    naive_calls += 1   # count every call
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive calls (repeated subproblems happen here)
    return fib_naive(n-1) + fib_naive(n-2)

# Memoized Fibonacci
memo_calls = 0  # counter for memoized calls
def fib_memo(n, memo={}):
    global memo_calls
    memo_calls += 1
    # If value already calculated, return directly
    if n in memo:
        return memo[n]
    if n == 0:
        memo[n] = 0
    elif n == 1:
        memo[n] = 1
    else:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)

    return memo[n]

# Main Program
n = int(input("Enter number: "))

# Reset counters
naive_calls = 0
memo_calls = 0

print("\nNaive Fibonacci Series:")
for i in range(n):
    print(fib_naive(i), end=" ")

print("\nNaive Call Count:", naive_calls)

print("\nMemoized Fibonacci Series:")
for i in range(n):
    print(fib_memo(i, {}), end=" ")

print("\nMemoized Call Count:", memo_calls)



