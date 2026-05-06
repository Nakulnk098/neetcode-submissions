class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        r = l = 0
        q = deque() #we are appending the index istead of the number 

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]: # here it takes the last most element of the queue and compares with the current r index on nums and if nums of r is greater?then it removes the last index value of the q and so on
                q.pop()
            q.append(r)

            #once we add the element form q to output, when we add a new element the old element form q should be removed
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output


