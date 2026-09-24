import heapq

class Solution:
    def kClosest(self, points, k):
        list1 = []

        for a, b in points:
            distance = a**2 + b**2
            list1.append((distance, [a, b]))

        heapq.heapify(list1)

        result = []

        for _ in range(k):
            distance, point = heapq.heappop(list1)
            result.append(point)

        return result