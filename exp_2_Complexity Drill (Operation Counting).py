# Experiment 2:
    #Complexity Drill (Operation Counting)
# Aim:
    #Develop intuition for time/space complexity using simple loop structures and case analysis.
# What you will implement (in lab):
    #Create 4 snippets: single loop, nested loop, triangular loop, and halving loop. Count operations roughly and map to Big-O. Add best/avg/worst reasoning for linear search and
    #binary search.
# Input / Output expectation:
    #Input: n. Output: for each snippet print estimated operation count + complexity label+ 2-line justification.
# Lab checkpoints (faculty verifies):
    #• Correct mapping for O(1), O(n), O(n2), O(logn)
    #• Clear best/avg/worst definitions with examples
# Viva:
    #1. Big-O vs Big-Theta difference?
    #2. What does worst-case represent?
    #3. Why complexity matters in real systems?





# SOLUTION :
# 1. Single Loop
# This loop runs exactly n times.
# So operation count increases linearly.
# Therefore time complexity = O(n)

def single_loop(n):
    count = 0                 
    for i in range(n):        
        count += 1            
    return count


# 2. Nested Loop
# Outer loop runs n times.
# Inner loop also runs n times.
# Total operations = n * n = n^2
# Therefore complexity = O(n^2)

def nested_loop(n):
    count = 0
    for i in range(n):        
        for j in range(n):    
            count += 1
    return count


# 3. Triangular Loop
# Inner loop runs from 0 to i.
# Total operations = n(n+1)/2
# Which simplifies to ~ n^2/2
# Dominant term is n^2
# Therefore complexity = O(n^2)

def triangular_loop(n):
    count = 0
    for i in range(n):
        for j in range(i + 1):
            count += 1
    return count


# 4. Halving Loop
# Each iteration divides n by 2.
# Number of times we can divide n by 2
# until it becomes 1 is log2(n).
# Therefore complexity = O(log n)

def halving_loop(n):
    count = 0
    while n > 1:
        n = n // 2            
        count += 1
    return count

# Main Program
# Input: value of n
# Output: operation count + complexity explanation

if __name__ == "__main__":

    n = int(input("Enter value of n: "))

    # Single Loop
    c1 = single_loop(n)
    print("\nSingle Loop:")
    print("Operation Count:", c1)
    print("Complexity: O(n)")
    print("Reason: Loop runs exactly n times.\n")

    # Nested Loop
    c2 = nested_loop(n)
    print("Nested Loop:")
    print("Operation Count:", c2)
    print("Complexity: O(n^2)")
    print("Reason: n * n iterations.\n")

    # Triangular Loop
    c3 = triangular_loop(n)
    print("Triangular Loop:")
    print("Operation Count:", c3)
    print("Complexity: O(n^2)")
    print("Reason: Total operations = n(n+1)/2.\n")

    # Halving Loop
    c4 = halving_loop(n)
    print("Halving Loop:")
    print("Operation Count:", c4)
    print("Complexity: O(log n)")
    print("Reason: Value reduces by half each time.\n")


