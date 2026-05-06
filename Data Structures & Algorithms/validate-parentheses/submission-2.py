class Solution:
    def isValid(self, s: str) -> bool:
        lefty = "({["
        righty = ")}]"
        stack = []

        for i in s:
            if i in lefty:
                stack.append(i)
            elif i in righty:
                if not stack:
                    return False
                if righty.index(i) != lefty.index(stack.pop()):
                    return False

        return not stack
                 