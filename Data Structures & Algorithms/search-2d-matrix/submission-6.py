class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            low = 0
            high = len(i) - 1
            while low <= high:
                mid = (low + high) // 2
                if i[mid] < target:
                    low = mid + 1
                elif i[mid] > target:
                    high = mid - 1
                else:
                    return True
            continue
        return False