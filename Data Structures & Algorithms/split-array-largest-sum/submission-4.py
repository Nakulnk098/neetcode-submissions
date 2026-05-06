class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            # subarray doesnt start with zero so hence 1 and when you pack items in a box its considered as 1 box not zer :)
            #if subarray less than of k that means we are not going above k constraint 
            subarray = 1
            curSum = 0
            for num in nums:
                curSum += num
                if curSum > largest:
                    subarray += 1
                    if subarray > k:
                        return False
                    curSum = num
            return True

        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            mid = l + (r - l) // 2
            if canSplit(mid):
                res = mid
                r = mid - 1 #just go below the actual mid value cause we already know that its lowest maximun value rather than doing it with same value
            else:
                l = mid + 1
        return res

