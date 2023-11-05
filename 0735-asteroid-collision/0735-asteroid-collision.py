class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        
        for asteroid in asteroids[1:]:
            if not stack:
                stack.append(asteroid)
            else:
                while stack and asteroid < 0 < stack[-1]:
                    top = stack.pop()
                    if abs(top) == abs(asteroid):
                        break
                    elif abs(top) > abs(asteroid):
                        stack.append(top)
                        break
                else:
                    stack.append(asteroid)

        return stack







                
            
            
            
            
        
        