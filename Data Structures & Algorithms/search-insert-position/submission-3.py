class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target: # Target is in the right half, so search above mid
                low = mid + 1
            elif nums[mid] > target:# Target is in the left half, so search below mid
                high = mid - 1
            else:
                return mid  
        return low 

# same as the original problem where we just do return left why?
#cause if the original value is not found it is most likely present in the left most pointer 
#cause if you do right it is technically out of bounds so either (MID OR LEFT)