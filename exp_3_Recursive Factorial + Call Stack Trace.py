# Experiment 3:
    #Recursive Factorial + Call Stack Trace
# Aim :
    #Learn recursion basics: base case, recursive case, and stack growth.
# What you will implement (in lab):
    #Implement factorial(n) recursively for n≥0 and reject invalid input. Draw call stack for
    #factorial(4) showing return values.
# Input / Output expectation :
    #Input: n. Output: factorial(n) + manual call stack trace (in notebook) + time/space
    #complexity statement.
# Lab checkpoints (faculty verifies) :
    #• Base case correct, recursion correct
    #• Complexity stated correctly: time O(n), space O(n)
# Viva :
    #1. What is recursion depth?
    #2. Why recursion uses stack memory?
    #3. When iteration is better than recursion?




# SOLUTION :
# Factorial Formula:
# n! = n × (n-1)!
# Base case: 0! = 1


def factorial(n):
    # Reject invalid input
    if n < 0:
        return "Invalid input: factorial not defined for negative numbers"

    # Base Case:
    # When n == 0, recursion stops
    if n == 0:
        return 1

    # Recursive Case:
    # Function calls itself with smaller value
    return n * factorial(n - 1)



# Main Program
if __name__ == "__main__":

    n = int(input("Enter a non-negative integer: "))

    result = factorial(n)

    print("Factorial of", n, "=", result)



# Time Complexity:
# Each call reduces n by 1
# Total calls = n
# Therefore Time Complexity = O(n)
#
# Space Complexity:
# Each recursive call is stored in call stack
# Maximum depth = n
# Therefore Space Complexity = O(n)
