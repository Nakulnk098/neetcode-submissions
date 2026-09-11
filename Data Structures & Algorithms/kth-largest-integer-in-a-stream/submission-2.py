class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        #heapify converts a normal list to heap list where the first position of the heap will always have smallest value in it.
        heapq.heapify(self.minHeap)
        #at beginning to check if the length of the list is greater than k, if it is we need to make sure that its at the same exact values of k
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
