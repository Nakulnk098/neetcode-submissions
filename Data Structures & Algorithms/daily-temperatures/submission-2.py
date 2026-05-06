class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
      n = len(temperatures)
      res = [0] * (n)
      stack = [] #temp, index

      for i,t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            cur_temp, cur_index = stack.pop()
            res[cur_index] = i - cur_index
        stack.append((t,i))
      return res
      
