class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)

    def pop(self) -> None:
        if self.isEmpty():
            return None
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        if self.isEmpty():
            return "Stack is empty!!"
        return self.stack[-1]

    def getMin(self) -> int:
        if self.isEmpty():
            return None
        # return min(self.stack)
        return self.minstack[-1]
    

stack = MinStack()
# isEmpty operation
print("Is stack empty?:", stack.isEmpty())
# size operation
print("Size of stack:", stack.size())
# push operation
stack.push(5)
stack.push(2)
stack.push(8)
print("Top element after pushes:", stack.top())
print("Minimum element after pushes:", stack.getMin())
# pop operation
stack.pop()
print("Top element after pop:", stack.top())
print("Minimum element after pop:", stack.getMin())