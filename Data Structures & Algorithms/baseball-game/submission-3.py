class Solution:
    def calPoints(self, operations: List[str]) -> int:
        plus = "+"
        d = "D"
        c = "C"
        stack = []
        for i in operations:
            if i == plus:
                count = stack[-1] + stack[-2]
                stack.append(count)
            elif i == c:
                stack.pop()
            elif i == d:
                num = stack[-1]
                new_num = num * 2
                stack.append(new_num)
            else:
                stack.append(int(i))
        return sum(stack)