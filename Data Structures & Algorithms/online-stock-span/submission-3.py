class StockSpanner:

    def __init__(self):
        self.stack = [] #price, span

    def next(self, price: int) -> int:
        span = 1
        while self.stack and price >= self.stack[-1][0]:
            new_price, new_span = self.stack.pop()
            span += new_span
        self.stack.append((price, span))
        return span

stockSpanner = StockSpanner()

stockSpanner.next(100) # 1
stockSpanner.next(80)   # 1
stockSpanner.next(60)   # 1
stockSpanner.next(70)  # 2
stockSpanner.next(60)   # 1
stockSpanner.next(75)   # 4
stockSpanner.next(85)   # 6



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)