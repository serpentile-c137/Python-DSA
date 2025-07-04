class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0
    
    def size(self):
        return self.size
    
    def push(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def print(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        
        itr = self.head
        stack_str = ''
        while itr:
            stack_str += str(itr.data) + ' --> '
            itr = itr.next
        print(stack_str[:-5])

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty!!")
        
        pop_ele = self.head.data
        self.head = self.head.next
        self.size -= 1
        return pop_ele

if __name__ == "__main__":
    stack = Stack()
    print("Is stack empty?", stack.isEmpty())
    print("Stack size:", stack.size)
    stack.push(0)
    stack.push(1)
    stack.push(2)
    print("Is stack empty?", stack.isEmpty())
    print("Stack size:", stack.size)
    stack.print()
    print("Popped element:", stack.pop())
    stack.print()


# Output:

# Is stack empty? True
# Stack size: 0
# Is stack empty? False
# Stack size: 3
# 2 --> 1 --> 0
# Popped element: 2
# 1 --> 0