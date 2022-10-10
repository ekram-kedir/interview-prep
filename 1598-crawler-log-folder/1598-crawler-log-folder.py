class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        for i in logs:
            if stack and i=="../":
                stack.pop()
            elif i=="./":
                continue
            elif i!="../":
                stack.append(i)
        return len(stack)