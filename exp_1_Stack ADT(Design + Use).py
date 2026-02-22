# 2.1. Experiment 1: Stack ADT (Design + Use)
# Aim
     # Design a Stack ADT and build confidence in LIFO behavior and constant-time operations.
# What you will implement (in lab)
    # Implement StackADT with push, pop, peek, isEmpty, size. Use it once meaningfully (e.g.,
    # store steps of recursion trace, undo operations, or expression symbols).
# Input / Output expectation
    # Input: sequence of operations. Output: returned values (pop/peek) + final stack state
    # + safe underflow handling.
# Lab checkpoints (faculty verifies)
    # • All operations behave correctly (LIFO)
    # • Underflow handled safely (no crash)
    # • Stack used in a small real task (not only basic testing)
# Viva (answer any 3)
    # 1. What is an ADT?
    # 2. Why push/pop can be O(1)?
    # 3. One real-world use of stack?




# SOLUTION :
# Stack is an Abstract Data Type (ADT)
# It follows LIFO (Last In First Out) principle.
class StackADT:
    def __init__(self):
        # Internal storage using list
        self.data = []

    # Push operation (insert at top)
    def push(self, value):
        self.data.append(value)     # O(1)

    # Pop operation (remove from top)
    def pop(self):
        if self.isEmpty():
            return "Underflow: Stack is empty"
        return self.data.pop()      # O(1)

    # Peek operation (view top element)
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.data[-1]

    # Check if stack is empty
    def isEmpty(self):
        return len(self.data) == 0

    # Return size of stack
    def size(self):
        return len(self.data)

    # Display full stack
    def display(self):
        return self.data



# Meaningful Use: Reversing a String using Stack
def reverse_string(text):
    stack = StackADT()

    for ch in text:
        stack.push(ch)

    reversed_text = ""
    while not stack.isEmpty():
        reversed_text += stack.pop()

    return reversed_text



# Main Program (Sequence of Operations)
if __name__ == "__main__":

    stack = StackADT()

    print("Pushing elements: 10, 20, 30")
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Current Stack:", stack.display())

    print("Peek:", stack.peek())       # Should return 30 (LIFO)
    print("Pop:", stack.pop())         # Removes 30

    print("Stack after pop:", stack.display())

    print("Popping all elements...")
    print(stack.pop())
    print(stack.pop())

    # Underflow case
    print(stack.pop())   # Stack empty now

    print("Final Stack State:", stack.display())

    # Meaningful Use
    text = input("Enter a string to reverse: ")
    print("Reversed String:", reverse_string(text))

# Complexity:
# push()  -> O(1)
# pop()   -> O(1)
# peek()  -> O(1)
