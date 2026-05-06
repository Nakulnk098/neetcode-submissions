class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        count = []
        if len(arr) == k:
            print(arr)

        for i in range(len(arr)):
            b = abs(arr[i] - x)
            count.append((b, arr[i]))   

        new_count = sorted(count)

        new = []
        for i in range(k):
            new.append(new_count[i][1])  

        new.sort()  

        return new
