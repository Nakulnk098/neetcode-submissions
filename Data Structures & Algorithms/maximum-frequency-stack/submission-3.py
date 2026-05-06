class FreqStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> int:
        freq = {}
        for i in self.stack:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        max_value = max(freq.values())
        candidates = [k for k,v in freq.items() if v == max_value]
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i] in candidates:
                return self.stack.pop(i)
               
fs = FreqStack()

fs.push(5)
fs.push(7)
fs.push(5)
fs.push(7)
fs.push(4)
fs.push(5)

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()