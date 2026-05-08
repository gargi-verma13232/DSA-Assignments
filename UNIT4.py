# =========================================================
# UNIT 4 ASSIGNMENT
# Non-Linear & Advanced Data Structures
# =========================================================


# =========================================================
# EXPERIMENT 20 & 21
# BST INSERT / SEARCH / DELETE / INORDER
# =========================================================

class BSTNode:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None

    # INSERT
    def insert(self, root, key):

        if root is None:
            return BSTNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        return root

    # SEARCH
    def search(self, root, key):

        if root is None or root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)

        return self.search(root.right, key)

    # INORDER
    def inorder(self, root):

        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    # FIND MINIMUM VALUE
    def min_value_node(self, node):

        current = node

        while current.left is not None:
            current = current.left

        return current

    # DELETE
    def delete(self, root, key):

        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)

        elif key > root.key:
            root.right = self.delete(root.right, key)

        else:

            # CASE 1: NO CHILD
            if root.left is None and root.right is None:
                return None

            # CASE 2: ONE CHILD
            elif root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            # CASE 3: TWO CHILDREN
            temp = self.min_value_node(root.right)

            root.key = temp.key

            root.right = self.delete(root.right, temp.key)

        return root


# =========================================================
# BST DEMO
# =========================================================

print("\n================ BST OPERATIONS ================")

bst = BST()

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    bst.root = bst.insert(bst.root, value)

print("\nInorder Traversal:")
bst.inorder(bst.root)

print("\n\nSearching 40:")

if bst.search(bst.root, 40):
    print("40 Found")
else:
    print("40 Not Found")

print("\nDeleting 20")
bst.root = bst.delete(bst.root, 20)

print("Inorder After Deletion:")
bst.inorder(bst.root)


# =========================================================
# EXPERIMENT 22
# HEAP / PRIORITY QUEUE
# =========================================================

import heapq

print("\n\n================ HEAP / PRIORITY QUEUE ================")

heap = []

numbers = [40, 10, 30, 50, 20]

for num in numbers:
    heapq.heappush(heap, num)

print("\nHeap Elements:")
print(heap)

print("\nExtracting Elements:")

while heap:
    print(heapq.heappop(heap), end=" ")


# =========================================================
# EXPERIMENT 23
# GRAPH USING ADJACENCY LIST
# =========================================================

print("\n\n================ GRAPH ADJACENCY LIST ================")

graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 7), ('E', 1)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 5)],
    'F': []
}

for node in graph:
    print(node, "->", graph[node])


# =========================================================
# EXPERIMENT 24
# BFS TRAVERSAL
# =========================================================

from collections import deque

print("\n================ BFS TRAVERSAL ================")

def bfs(graph, start):

    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:

        node = queue.popleft()

        print(node, end=" ")

        for neighbor, weight in graph[node]:

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


print("\nBFS Starting from A:")
bfs(graph, 'A')


# =========================================================
# EXPERIMENT 25
# DFS TRAVERSAL
# =========================================================

print("\n\n================ DFS TRAVERSAL ================")

visited = set()

def dfs(graph, node):

    if node not in visited:

        print(node, end=" ")

        visited.add(node)

        for neighbor, weight in graph[node]:
            dfs(graph, neighbor)


print("\nDFS Starting from A:")
dfs(graph, 'A')


# =========================================================
# EXPERIMENT 26
# HASH TABLE WITH SEPARATE CHAINING
# =========================================================

print("\n\n================ HASH TABLE ================")

class HashTable:

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):

        index = self.hash_function(key)

        self.table[index].append((key, value))

    def get(self, key):

        index = self.hash_function(key)

        for k, v in self.table[index]:

            if k == key:
                return v

        return "Not Found"

    def delete(self, key):

        index = self.hash_function(key)

        for i, (k, v) in enumerate(self.table[index]):

            if k == key:
                del self.table[index][i]
                return

    def display(self):

        for i, bucket in enumerate(self.table):
            print(i, "->", bucket)


ht = HashTable(5)

ht.insert(1, "Apple")
ht.insert(6, "Banana")
ht.insert(11, "Orange")

print("\nHash Table:")
ht.display()

print("\nGet Key 6:")
print(ht.get(6))

print("\nDelete Key 6")
ht.delete(6)

print("\nHash Table After Deletion:")
ht.display()


# =========================================================
# EXPERIMENT 27
# TRIE (PREFIX TREE)
# =========================================================

print("\n\n================ TRIE ================")

class TrieNode:

    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):

        node = self.root

        for char in word:

            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.end_of_word = True

    def search(self, word):

        node = self.root

        for char in word:

            if char not in node.children:
                return False

            node = node.children[char]

        return node.end_of_word

    def starts_with(self, prefix):

        node = self.root

        for char in prefix:

            if char not in node.children:
                return False

            node = node.children[char]

        return True


trie = Trie()

words = ["apple", "app", "bat"]

for word in words:
    trie.insert(word)

print("\nSearch 'apple':", trie.search("apple"))
print("Search 'bat':", trie.search("bat"))
print("Prefix 'ap':", trie.starts_with("ap"))
print("Prefix 'ba':", trie.starts_with("ba"))


# =========================================================
# EXPERIMENT 28
# BLOOM FILTER (TOY DEMO)
# =========================================================

print("\n\n================ BLOOM FILTER ================")

size = 10
bit_array = [0] * size

def hash1(item):
    return len(item) % size

def hash2(item):
    return sum(ord(c) for c in item) % size

def add(item):

    bit_array[hash1(item)] = 1
    bit_array[hash2(item)] = 1

def check(item):

    if bit_array[hash1(item)] == 1 and bit_array[hash2(item)] == 1:
        return "Possibly Present"

    return "Definitely Not Present"


add("apple")
add("banana")

print("\nBit Array:")
print(bit_array)

print("\nCheck 'apple':")
print(check("apple"))

print("\nCheck 'grape':")
print(check("grape"))


# =========================================================
# THEORY NOTES
# =========================================================

print("\n\n================ THEORY NOTES ================")

print("""
1. BST
   - Average Search Complexity : O(log n)
   - Worst Case                : O(n)

2. Heap / Priority Queue
   - Insert  : O(log n)
   - Delete  : O(log n)

3. BFS
   - Uses Queue
   - Traverses level by level

4. DFS
   - Uses Recursion or Stack
   - Traverses depth-wise

5. Hash Table
   - Average Complexity : O(1)
   - Collision handled using chaining

6. Trie
   - Efficient for prefix searching
   - Used in autocomplete systems

7. Bloom Filter
   - Probabilistic data structure
   - May give false positives
   - Never gives false negatives
""")