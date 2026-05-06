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