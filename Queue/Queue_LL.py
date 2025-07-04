class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def size(self):
        return self.size
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def print(self):
        if self.isEmpty():
            print("Queue is empty!!")
            return
        itr = self.head
        queue_str = ''
        while itr:
            queue_str += str(itr.data) + ' <-- '
            itr = itr.next
        print(queue_str[:-5])

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty!!")
        
        dequeue_ele = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return dequeue_ele



if __name__ == "__main__":
    queue = Queue()
    print("Is queue empty?", queue.isEmpty())
    print("Queue size:", queue.size)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(10)
    queue.enqueue(20)
    print("Is queue empty?", queue.isEmpty())
    print("Queue size:", queue.size)
    queue.print()
    print("Dequeued element:", queue.dequeue())
    queue.print()
    print("Dequeued element:", queue.dequeue())
    queue.print()
    
# Output: 

#  Is queue empty? True
# Queue size: 0
# Is queue empty? False
# Queue size: 5
# 1 <-- 2 <-- 3 <-- 10 <-- 20
# Dequeued element: 1
# 2 <-- 3 <-- 10 <-- 20
# Dequeued element: 2
# 3 <-- 10 <-- 20
