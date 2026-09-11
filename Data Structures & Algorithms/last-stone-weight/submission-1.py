class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 1)to get the samllest values in heap , the first value is always the smallest one and so on..
        # 2)to find the greatest value in the heap, we need to do the reverse of it, where we apply - values to the, so that the greatest is present in first postion itself having the - sign
        stones = [-s for s in stones]
        heapq.heapify(stones)

        # if second > first , add the remanning in the stones
        # if equal tboth are automatically removed 
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        #if all the stones were removed to make sure that atleast one is number is present which is zero
        stones.append(0)
        return abs(stones[0])