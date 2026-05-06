class Solution:
    def findMin(self, nums: List[int]) -> int:
        n= len(nums)
        low = 0
        high = n - 1
        #essentially we are trying to find smallest element from the list but there is a catch
        # in the program we are trying to find the point at which index did the stair change
        #ex = [3,4,5,6,1,2] after index 3 the stair has changed and we are trying to find the first element from the new change of stair case
        # the first element of that change of stair is always going to be small (cause they are ordered and are unique)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] < nums[high]:
                high = mid
            else: 
                low = mid + 1
        return nums[low]
