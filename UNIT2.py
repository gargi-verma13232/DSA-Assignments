# ==============================
# 1. DYNAMIC ARRAY
# ==============================
class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.arr = [0] * self.capacity

    def append(self, value):
        if self.size == self.capacity:
            self._resize()

        self.arr[self.size] = value
        self.size += 1

    def _resize(self):
        self.capacity *= 2
        new_arr = [0] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def pop(self):
        if self.size == 0:
            print("Array Underflow")
            return None
        val = self.arr[self.size - 1]
        self.size -= 1
        return val

    def display(self):
        print(self.arr[:self.size])


# ==============================
# 2. SINGLY LINKED LIST (SLL)
# ==============================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def insert_end(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def delete(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp:
            prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# ==============================
# 3. DOUBLY LINKED LIST (DLL)
# ==============================
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new = DNode(data)
        if self.head:
            self.head.prev = new
            new.next = self.head
        self.head = new

    def insert_end(self, data):
        new = DNode(data)
        if not self.head:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new
        new.prev = temp

    def delete(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                return
            temp = temp.next

    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def display_backward(self):
        temp = self.head
        if not temp:
            return
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")


# ==============================
# 4. STACK USING SLL
# ==============================
class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new = Node(data)
        new.next = self.top
        self.top = new

    def pop(self):
        if not self.top:
            print("Stack Underflow")
            return None
        val = self.top.data
        self.top = self.top.next
        return val

    def peek(self):
        return self.top.data if self.top else None


# ==============================
# 5. QUEUE USING SLL
# ==============================
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new = Node(data)
        if not self.rear:
            self.front = self.rear = new
            return
        self.rear.next = new
        self.rear = new

    def dequeue(self):
        if not self.front:
            print("Queue Underflow")
            return None
        val = self.front.data
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return val


# ==============================
# 6. PARENTHESES CHECKER
# ==============================
def is_valid(expression):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0


# ==============================
# DEMONSTRATION (IMPORTANT)
# ==============================
if __name__ == "__main__":

    print("---- Dynamic Array ----")
    da = DynamicArray()
    da.append(10)
    da.append(20)
    da.append(30)
    da.display()
    print("Pop:", da.pop())
    da.display()

    print("\n---- SLL ----")
    sll = SLL()
    sll.insert_begin(10)
    sll.insert_end(20)
    sll.insert_end(30)
    sll.display()
    sll.delete(20)
    sll.display()

    print("\n---- DLL ----")
    dll = DLL()
    dll.insert_begin(1)
    dll.insert_end(2)
    dll.insert_end(3)
    dll.display_forward()
    dll.display_backward()

    print("\n---- Stack ----")
    st = Stack()
    st.push(5)
    st.push(10)
    print("Pop:", st.pop())

    print("\n---- Queue ----")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print("Dequeue:", q.dequeue())

    print("\n---- Parentheses Checker ----")
    exp = "{[()]}"
    print("Valid" if is_valid(exp) else "Invalid")