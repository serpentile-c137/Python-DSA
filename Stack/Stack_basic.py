stack = [] # empty stack using python list

# push operation
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
# Displaying the current stack
print("Current stack:", stack)

# pop operation
top_ele = stack.pop()
print("Popped element:", top_ele)

# Displaying the current stack
print("Current stack:", stack)

# peek operation
top_ele = stack[-1]
print("Top element:", top_ele)

# is_empty operation
isEmpty = not bool(stack)
print("Is stack empty?: ", isEmpty)

# size operation
size = len(stack)
print("Size of stack:", size)

# Displaying the current stack
print("Current stack:", stack)