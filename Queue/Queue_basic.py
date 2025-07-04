queue = []

# Enqueue operation
queue.append(0)
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
# Displaying the current queue
print("queue:", queue)

# Peek operation
front = queue[0]
print("Peek: ", front)

# Dequeue operation
pop_ele = queue.pop(0)
print("Dequeued element:", pop_ele)

# isEmpty operation
isEmpty = not bool(queue)
print("Is queue empty?: ", isEmpty)

# Size operation
size = len(queue)
print("Size: ", size)

# Output:

# queue: [0, 1, 2, 3, 4]
# Peek:  0
# Dequeued element: 0
# Is queue empty?:  False
# Size:  4