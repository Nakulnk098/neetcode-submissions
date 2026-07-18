class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            if i > 0:
                stack.append(i)
            else:
                while stack and stack[-1] > 0:
                    if stack[-1] == abs(i):
                        stack.pop()
                        break
                    elif stack[-1] < abs(i):
                        stack.pop()
                        continue
                    else:
                        break
                else:
                    stack.append(i)
        return stack
                    
     
                    

                    
                    

            
