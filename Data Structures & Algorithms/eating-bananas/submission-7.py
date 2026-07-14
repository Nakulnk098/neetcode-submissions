import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        high = max(piles)
        while l < high:
            mid = (l + high)//2
            total_hour = 0
            for pile in piles:
                total_hour += math.ceil(pile/mid)

            if total_hour <= h:
                high = mid
            else:
                l = mid + 1
        return l
        