class Stack:
    # constructor to initialize the stack
    def __init__(self):
        self.stack = []
    
    # isEmpty method to check if the stack is empty
    def isEmpty(self):
        return len(self.stack) == 0
    
    # size method to return the number of elements in the stack
    def size(self):
        return len(self.stack)
    
    # push method to add an element to the stack
    def push(self, ele):
        self.stack.append(ele)

    # pop method to remove and return the top element of the stack
    def pop(self):
        if self.isEmpty():
            return "Stack is empty!!"
        return self.stack.pop()
    
    # peek method to return the top element of the stack without removing it
    def peek(self):
        if self.isEmpty():
            return "Stack is empty!!"
        return self.stack[-1]
    
    def display(self):
        return self.stack
    

#creating an instance of Stack class
stack = Stack()

#isEmpty operation
print("Is stack empty?:", stack.isEmpty())

# pushing elements onto the stack
stack.push(1)
stack.push(2)
stack.push(3)

# displaying the current stack
print("Current stack:", stack.display())

# popping an element from the stack
top_ele = stack.pop()
print("Popped element:", top_ele)
print("Current stack:", stack.display())

stack.push(4)
stack.push(5)
print("Current stack after pushing 4 and 5:", stack.display())

# peek operation
top_ele = stack.peek()
print("Top element:", top_ele)

# size operation
print("Size of stack:", stack.size())
