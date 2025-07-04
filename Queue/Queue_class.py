class Queue:
    # constructor to initialize the stack
    def __init__(self):
        self.queue = []
    
    # isEmpty method to check if the stack is empty
    def isEmpty(self):
        return len(self.queue) == 0
    
    # size method to return the number of elements in the stack
    def size(self):
        return len(self.queue)
    
    # push method to add an element to the stack
    def enqueue(self, ele):
        self.queue.append(ele)

    # pop method to remove and return the top element of the stack
    def dequeue(self):
        if self.isEmpty():
            return "Stack is empty!!"
        return self.queue.pop(0)
    
    # peek method to return the top element of the stack without removing it
    def peek(self):
        if self.isEmpty():
            return "Stack is empty!!"
        return self.queue[0]
    
    def display(self):
        return self.queue
    

#creating an instance of queue class
queue = Queue()

#isEmpty operation
print("Is queue empty?:", queue.isEmpty())

# pushing elements onto the stack
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# displaying the current queue
print("Current queue:", queue.display())

# popping an element from the queue
top_ele = queue.dequeue()
print("Popped element:", top_ele)
print("Current stack:", queue.display())

queue.enqueue(4)
queue.enqueue(5)
print("Current stack after pushing 4 and 5:", queue.display())

# peek operation
top_ele = queue.peek()
print("Top element:", top_ele)

# size operation
print("Size of queue:", queue.size())


# Output:

# Is queue empty?: True
# Current queue: [1, 2, 3]
# Popped element: 1
# Current stack: [2, 3]
# Current stack after pushing 4 and 5: [2, 3, 4, 5]
# Top element: 2
# Size of queue: 4
