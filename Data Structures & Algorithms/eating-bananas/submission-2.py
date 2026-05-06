import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low < high:
            mid = (low + high) // 2
            
            total_hour = 0
            for pile in piles:
                total_hour += math.ceil(pile/mid)
            
            if total_hour <= h:
                high = mid
            else: 
                low = mid + 1
        return low
    