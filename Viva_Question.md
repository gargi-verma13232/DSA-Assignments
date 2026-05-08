# Data Structures Viva Questions & Answers
# All Units Combined

---

# UNIT 1 : Foundations & Algorithmic Analysis

---

# Experiment 1 : Stack ADT

## Q1. What is an ADT?

### Answer:
ADT (Abstract Data Type) is a logical model of a data structure that defines operations without showing implementation details.

Examples:
- Stack
- Queue
- List

---

## Q2. Why are push and pop O(1)?

### Answer:
Push and pop operate only at the top of the stack.

No traversal is required, so operations take constant time.

### Complexity:
O(1)

---

## Q3. One real-world use of stack?

### Answer:
Real-world uses:
- Browser back button
- Undo/Redo
- Function call handling
- Expression evaluation

---

# Experiment 2 : Complexity Drill

## Q1. Big-O vs Big-Theta difference?

### Answer:
- Big-O represents upper bound.
- Big-Theta represents exact bound.

Example:
If an algorithm always takes n² time:
- O(n²)
- Θ(n²)

---

## Q2. What does worst-case represent?

### Answer:
Worst-case means maximum time taken by an algorithm for any input.

It represents the slowest possible execution.

---

## Q3. Why does complexity matter in real systems?

### Answer:
Complexity helps:
- Reduce execution time
- Save memory
- Improve scalability
- Handle large datasets efficiently

---

# Experiment 3 : Recursive Factorial

## Q1. What is recursion depth?

### Answer:
Recursion depth is the number of recursive function calls present in the call stack.

---

## Q2. Why does recursion use stack memory?

### Answer:
Each recursive call is stored in stack memory until it returns.

---

## Q3. When is iteration better than recursion?

### Answer:
Iteration is better when:
- Memory usage must be low
- Recursion depth is very large
- Performance is important

---

# Experiment 4 : Fibonacci

## Q1. Why is naive Fibonacci slow?

### Answer:
Because it repeatedly calculates the same subproblems.

This creates many unnecessary recursive calls.

---

## Q2. Is memoization related to Dynamic Programming?

### Answer:
Yes.

Memoization stores previously computed results, which is a technique used in Dynamic Programming.

---

## Q3. What is the space impact of memoization?

### Answer:
Memoization uses extra memory to store computed values.

Space Complexity:
O(n)

---

# Experiment 5 : Tower of Hanoi

## Q1. Why are moves 2ⁿ − 1?

### Answer:
Each recursive step doubles the previous moves and adds one extra move.

### Formula:
2ⁿ − 1

---

## Q2. What is recursion tree idea?

### Answer:
A recursion tree visually shows recursive function calls and their branching structure.

---

## Q3. Practical risk of exponential algorithms?

### Answer:
Exponential algorithms become extremely slow for large inputs.

They consume huge execution time and resources.

---

# Experiment 6 : Recursive Binary Search

## Q1. Why is sorted data required?

### Answer:
Binary search works by dividing the array using comparisons.

Without sorting, correct division is impossible.

---

## Q2. Best, average and worst case?

### Answer:
- Best Case: O(1)
- Average Case: O(log n)
- Worst Case: O(log n)

---

## Q3. What does Divide & Conquer mean?

### Answer:
Divide & Conquer divides a problem into smaller subproblems, solves them recursively, then combines results.

---

# UNIT 2 : Linear Data Structures

---

# Experiment 7 : Arrays 1D

## Q1. Why is index access O(1)?

### Answer:
Array elements are stored in contiguous memory.

Address calculation is direct.

---

## Q2. Why is insertion at start O(n)?

### Answer:
All elements need shifting toward the right.

---

## Q3. Static vs Dynamic Arrays?

### Answer:
- Static Array: Fixed size
- Dynamic Array: Size can grow or shrink

---

# Experiment 8 : Arrays 2D

## Q1. Complexity of scanning a matrix?

### Answer:
For an n × m matrix:

Complexity:
O(nm)

---

## Q2. Real-world use of 2D arrays?

### Answer:
- Images
- Game boards
- Matrices
- Excel sheets

---

## Q3. What is row-wise memory layout?

### Answer:
Elements of each row are stored continuously in memory.

---

# Experiment 9 : Dynamic Array

## Q1. What is amortized complexity?

### Answer:
Average cost of operations over multiple executions.

---

## Q2. Why does doubling help?

### Answer:
Doubling reduces frequent resizing operations.

---

## Q3. Why is pop-end O(1)?

### Answer:
Last element removal needs no shifting.

---

# Experiment 10 : Singly Linked List

## Q1. Why is search O(n)?

### Answer:
Traversal may require checking every node.

---

## Q2. Why is insert-at-head O(1)?

### Answer:
Only head pointer changes.

---

## Q3. What is node structure?

### Answer:
A node contains:
- Data
- Pointer to next node

---

# Experiment 11 : Doubly Linked List

## Q1. DLL advantage over SLL?

### Answer:
Traversal is possible in both directions.

---

## Q2. Browser history mapping?

### Answer:
Browser back and forward operations use DLL.

---

## Q3. Why is deletion easier in DLL?

### Answer:
Previous node is directly accessible.

---

# Experiment 12 : Stack using SLL

## Q1. Why is stack ideal here?

### Answer:
Parentheses follow LIFO order.

---

## Q2. What fails in “([)]”?

### Answer:
Closing brackets mismatch opening brackets.

---

## Q3. What is underflow?

### Answer:
Removing element from an empty stack.

---

# Experiment 13 : Queue using SLL

## Q1. Why does BFS use queue?

### Answer:
Queue processes nodes level by level using FIFO order.

---

## Q2. What does FIFO mean?

### Answer:
First In First Out.

---

## Q3. One scheduling example?

### Answer:
Printer scheduling.

---

# UNIT 3 : Sorting Algorithms

---

# Experiment 14 : O(n²) Sorts

## Q1. Stable vs unstable sorting?

### Answer:
Stable sorting preserves order of equal elements.

---

## Q2. What is in-place sorting?

### Answer:
Sorting using very little extra memory.

---

## Q3. Why is O(n²) slow?

### Answer:
Operations grow quadratically with input size.

---

# Experiment 15 : Insertion Sort

## Q1. Worst-case input?

### Answer:
Reverse sorted array.

---

## Q2. Is insertion sort stable?

### Answer:
Yes.

---

## Q3. Space complexity?

### Answer:
O(1)

---

# Experiment 16 : Merge Sort

## Q1. Why is merge sort stable?

### Answer:
Equal elements preserve order during merging.

---

## Q2. Why extra memory?

### Answer:
Temporary arrays are created.

---

## Q3. Use of merge sort?

### Answer:
External sorting and databases.

---

# Experiment 17 : Quick Sort

## Q1. Worst case?

### Answer:
Already sorted array with poor pivot.

---

## Q2. Is quick sort stable?

### Answer:
No.

---

## Q3. Average complexity?

### Answer:
O(n log n)

---

# Experiment 18 : Heap Sort

## Q1. Why is heap sort unstable?

### Answer:
Equal elements may change order.

---

## Q2. Heap vs BST for Top-K?

### Answer:
Heap is more efficient.

---

## Q3. Real-world use?

### Answer:
Priority queues and scheduling.

---

# Experiment 19 : Benchmark Harness

## Q1. Why reverse is worst for insertion?

### Answer:
Maximum shifts occur.

---

## Q2. Why quick sort degrades on sorted data?

### Answer:
Unbalanced partitions occur.

---

## Q3. Why merge sort uses memory?

### Answer:
Temporary arrays are required.

---

# UNIT 4 : Non-Linear & Advanced Data Structures

---

# Experiment 20 : BST Insert/Search/Inorder

## Q1. Why does inorder give sorted output?

### Answer:
BST stores smaller values left and larger values right.

---

## Q2. Worst-case BST height?

### Answer:
O(n)

---

## Q3. Average complexity?

### Answer:
O(log n)

---

# Experiment 21 : BST Delete

## Q1. What is inorder successor?

### Answer:
Smallest value in right subtree.

---

## Q2. Why is delete tricky?

### Answer:
Tree structure must remain valid.

---

## Q3. How to verify correctness?

### Answer:
Check inorder traversal.

---

# Experiment 22 : Heap / Priority Queue

## Q1. Why heap for priority queues?

### Answer:
Efficient insertion and deletion.

---

## Q2. Insert/extract complexity?

### Answer:
O(log n)

---

## Q3. Industry use?

### Answer:
Scheduling and task management.

---

# Experiment 23 : Graph Adjacency List

## Q1. List vs Matrix?

### Answer:
Adjacency list saves memory for sparse graphs.

---

## Q2. Directed vs Undirected graph?

### Answer:
Directed graph has one-way edges.

Undirected graph has two-way edges.

---

## Q3. Weighted graph use?

### Answer:
Maps and shortest path systems.

---

# Experiment 24 : BFS Traversal

## Q1. Why queue in BFS?

### Answer:
Queue processes nodes level-wise.

---

## Q2. Relation with shortest path?

### Answer:
BFS finds shortest path in unweighted graphs.

---

## Q3. Why complexity O(V+E)?

### Answer:
Every vertex and edge is visited once.

---

# Experiment 25 : DFS Traversal

## Q1. DFS vs BFS?

### Answer:
DFS goes deep first.

BFS goes level by level.

---

## Q2. Recursion depth issue?

### Answer:
Deep recursion may cause stack overflow.

---

## Q3. Use case of DFS?

### Answer:
Cycle detection and path finding.

---

# Experiment 26 : Hash Table

## Q1. What is collision?

### Answer:
Two keys map to same index.

---

## Q2. Why does chaining work?

### Answer:
Multiple elements are stored in linked lists.

---

## Q3. What is load factor?

### Answer:
Number of elements / table size.

---

# Experiment 27 : Trie

## Q1. Trie vs hash map for prefix?

### Answer:
Trie supports efficient prefix search.

---

## Q2. Space trade-off?

### Answer:
Trie uses more memory.

---

## Q3. Autocomplete use?

### Answer:
Search engines and keyboards.

---

# Experiment 28 : Bloom Filter

## Q1. Can bloom filter have false negatives?

### Answer:
No.

It may have false positives only.

---

## Q2. Why memory efficient?

### Answer:
Uses compact bit arrays.

---

## Q3. Industry use?

### Answer:
Databases, caching and security systems.