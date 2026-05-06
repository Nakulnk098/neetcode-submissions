class MyStack:

    def __init__(self):
        self.S = []

    def push(self, x: int) -> None:
        self.S.append(x)

    def pop(self) -> int:
        if self.S:
            return self.S.pop()
        else:
            return "nothing to pop"

    def top(self) -> int:
        if self.S:
            return self.S[-1]
        else:
            return "no element at the top"

    def empty(self) -> bool:
        return len(self.S) == 0


# Usage
myStack = MyStack()
myStack.push(1)
myStack.push(2)

print(myStack.top())    # 2
print(myStack.pop())    # 2
print(myStack.empty())  # False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()