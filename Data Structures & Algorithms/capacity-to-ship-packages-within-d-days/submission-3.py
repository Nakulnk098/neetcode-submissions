from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Minimum capacity must be at least the heaviest package
        low = max(weights)
        # Minimum capacity must be at least the heaviest package
        high = sum(weights)

        while low < high:
            mid = (low + high) // 2

            # Calculate how many days are needed with this capacity
            days_needed = 1
            current_weight = 0

            for w in weights:
                # If adding this package exceeds capacity → new day
                if current_weight + w > mid:
                    days_needed += 1
                    current_weight = w # start new day with current package
                else:
                    current_weight += w # continue loading current day
                    
            # If we can ship within given days → try smaller capacity
            if days_needed <= days:
                high = mid
            # If we can ship within given days → try smaller capacity
            else:
                low = mid + 1

        return low
        
                
                
        