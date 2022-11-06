class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s=[[i,j] for i,j in zip(position,speed)]
        stack=[]
        for i,j in sorted(s)[::-1]:
            stack.append((target-i)/j)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)
        