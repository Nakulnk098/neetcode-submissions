class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+', '-', '*', '/']
        stack = []
        for i in tokens:
            if i in ops:
                num2 = stack.pop()
                num1 = stack.pop()
                if i == "+":
                    val = num1 + num2
                    stack.append(val)
                elif i == "-":
                    val1 = num1 - num2
                    stack.append(val1)
                elif i == "*":
                    val2 = num1 * num2
                    stack.append(val2)
                else:
                    val3 = int(num1 / num2)
                    stack.append(val3)
            else:
                stack.append(int(i))
        return stack[0]

            