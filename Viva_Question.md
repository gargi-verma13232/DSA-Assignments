
<!--UNIT-1-->
<!-- EXPERIMENT 1  -->
1. What is an ADT?
An Abstract Data Type (ADT) is a logical model that defines the data and the operations that can be performed on it without specifying how they are implemented internally.
For example, a Stack ADT defines operations like push and pop, but it does not specify whether it is implemented using an array or a list.

2. Why push/pop can be O(1)?
Push and pop operations are O(1) because elements are inserted and removed only from the top of the stack.
No shifting of elements is required, so the time taken remains constant.

3. One real-world use of stack?
A real-world example of stack is the Undo/Redo feature in a text editor.
The most recent action performed is the first one to be undone, following the LIFO principle.

<!-- EXPERIMENT 2  -->
1. Big-O vs Big-Theta difference?
Big-O notation represents the upper bound (worst-case growth) of an algorithm.
Big-Theta represents the exact or tight bound of the growth rate.
In simple terms, Big-O shows the maximum time, while Big-Theta shows the exact growth behavior.

2. What does worst-case represent?
Worst-case represents the maximum number of operations an algorithm may perform for any valid input of size n.
It helps in understanding the maximum possible running time.

3. Why complexity matters in real systems?
Time and space complexity matter because real systems handle large amounts of data.
Efficient algorithms reduce execution time, memory usage, and improve overall system performance.

<!-- EXPERIMENT 3  -->
1. What is recursion depth?
Recursion depth is the maximum number of recursive calls present in the call stack at a given time.

2. Why recursion uses stack memory?
Each recursive function call is stored in memory until it completes execution.
This memory structure is called the call stack.

3. When iteration is better than recursion?
Iteration is better when recursion depth is very large, as recursion may cause stack overflow.
Iterative solutions usually use less memory.

<!-- EXPERIMENT 4 -->
1. Why naive Fibonacci is slow?
The naive recursive Fibonacci algorithm recalculates the same subproblems multiple times.
This leads to exponential time complexity, approximately O(2ⁿ).

2. Memoization relates to DP?
Yes, memoization is a technique used in Dynamic Programming.
It stores previously computed results to avoid repeated calculations.

3. Space impact of memoization?
Memoization requires extra memory to store computed values.
Therefore, its space complexity becomes O(n).

<!-- EXPERIMENT 5 -->
1. Why moves are 2ⁿ − 1?
The recurrence relation for Tower of Hanoi is:
T(n) = 2T(n−1) + 1
Solving this gives T(n) = 2ⁿ − 1.
Hence, the number of moves grows exponentially.

2. What is recursion tree idea?
A recursion tree is a diagram that shows how recursive calls are expanded step by step.
It helps in visualizing the growth of function calls and analyzing complexity.

3. Practical risk of exponential algorithms?
Exponential algorithms grow very rapidly with input size.
Even small increases in input can make the algorithm extremely slow and impractical for real-world use.

<!-- EXPERIMENT 6 -->
1. Why sorted data is required?
Binary search works by comparing the middle element and deciding whether to search in the left or right half.
This decision is only correct when the data is sorted.

2. Best / Average / Worst case?
Best Case: O(1) – When the middle element is the target.
Average Case: O(log n)
Worst Case: O(log n) – When the element is found at the last level or not present.

3. Divide & Conquer meaning?
Divide and Conquer is a strategy where a problem is divided into smaller subproblems, solved recursively, and then combined to form the final solution.
Binary search is an example of this approach.   



<!--UNIT-2-->
<!--EXPERIMENT 1-->
1. Why index access is O(1)?

Because arrays store elements in contiguous memory, so the address of any element is calculated using:
base_address + index × size → no traversal needed → constant time.

2. Why insertion at start is O(n)?

All elements must be shifted one position right, so time increases linearly with number of elements.

3. Static vs Dynamic Arrays
Static Array	Dynamic Array
Fixed size	Resizable
Faster	Flexible
Memory allocated once	Resizes during runtime

<!--EXPERIMENT 2-->
1. Complexity of scanning a matrix?

For matrix of size n × m → O(n × m)

2. Real-world use of 2D arrays?
Images (pixels)
Game boards (chess, sudoku)
Tables (Excel, databases)
3. Memory layout idea (row-wise)

Elements are stored row by row in memory.
Example:

[1 2 3
 4 5 6]

Stored as: 1,2,3,4,5,6

<!--EXPERIMENT 3-->
1. What is amortized complexity?

Average time per operation over many operations.
Even if one operation is costly, overall average remains low.

2. Why doubling helps?

Doubling reduces number of resizes → total cost spread over many inserts → O(1) amortized

3. Why pop-end is O(1)?

Last element is removed directly → no shifting required.

<!--EXPERIMENT 4-->
1. Why search is O(n)?

Need to traverse nodes one by one → no direct access like arrays.

2. Why insert-at-head is O(1)?

Only pointer change:

new.next = head
head = new

No traversal needed.

<!--EXPERIMENT 5-->
1. DLL advantage over SLL?
Traversal in both directions
Easier deletion (no need to track previous node)
2. Browser history mapping?

DLL is used because:

Back → move to previous node
Forward → move to next node
3. Deletion ease in DLL

Node can be deleted using:

prev.next = next
next.prev = prev

No need to traverse to find previous.

<!--EXPERIMENT 5-->
1. Why stack is ideal here?

Because stack follows LIFO, which matches bracket matching:
Last opened → first closed.

2. What fails in "([)]"?

Order is wrong:

( matches ) but [ is inside → mismatch
Stack detects incorrect pairing.
3. Underflow meaning

Trying to pop/remove from empty stack or queue

<!--EXPERIMENT 6-->
1. BFS uses queue?

Because BFS processes nodes level by level, using FIFO order.

2. FIFO meaning?

First In First Out
First inserted element is removed first.

3. Scheduling example?
CPU scheduling
Print queue
Ticket booking system

<!--EXPERIMENT 7-->
1. Node structure

A node contains:

data → value
pointer/reference → address of next (and prev in DLL)

Example:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None