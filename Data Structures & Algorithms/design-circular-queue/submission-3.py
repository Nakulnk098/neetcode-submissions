class ListNode:
    def __init__(self, val: int = -1, next: "ListNode" = None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool: # add to tail (newest)
        if self.capacity == 0:
            return False

        new_node = ListNode(value)

        # no items in circular queue
        if not self.head:
            self.head = new_node
            self.tail = self.head
            self.head.next = self.tail
        else:
            self.tail.next = new_node
            self.tail.next.next = self.head
            self.tail = self.tail.next

        self.capacity -= 1

        return True

    def deQueue(self) -> bool: # take from head (oldest)
        if not self.head:
            return False

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head

        self.capacity += 1
        
        return True

    def Front(self) -> int:
        return self.head.val if self.head else -1

    def Rear(self) -> int:
        return self.tail.val if self.tail else -1

    def isEmpty(self) -> bool:
        return not self.head

    def isFull(self) -> bool:
        return self.capacity == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()