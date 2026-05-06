class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()

        if length < 3:
            return -1
        
        #here we are trying to find the peak value where it will first incerase and decrease at a particular point , so we are trying to find the point
        #after we find the mid point the target which we want could be in either left or right (so we always do with first LEFT BINARY SEARCH AND THEN RIGHT BINARY SEARCH IF WE DIDNT FIND IN LEFT SIDE) 
        l, r = 0, length - 1
        while l <= r:
            m = (r + l) // 2
            left, mid, right =  mountainArr.get(m-1), mountainArr.get(m), mountainArr.get(m+1)
            if left < mid < right:
                l = m + 1
            elif left > mid > right:
                r = m - 1
            else:
                break
        peak = m

        #left binary search 
        l, r = 0 , peak
        while l <= r:
            mid = (l + r) // 2
            value = mountainArr.get(mid)
            if value < target:
                l = mid + 1
            elif value > target:
                r = mid - 1
            else:
                return mid
        
        #left binary search 
        l, r = peak , length - 1
        while l <= r:
            mid = (l + r) // 2
            value = mountainArr.get(mid)
            if value < target:
                r = mid - 1
            elif value > target:
                l = mid + 1
            else:
                return mid
        
        return -1
