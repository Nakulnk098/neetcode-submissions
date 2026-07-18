class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if not self.queue:
            return "Queue is empty"
        return self.queue.pop(0)

    def peek(self) -> int:
        if not self.queue:
            return "Queue is empty"
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0

myQueue = MyQueue()

myQueue.push(1)
myQueue.push(2)

print(myQueue.peek())   # 1
print(myQueue.pop())    # 1
print(myQueue.empty())  # False   


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()