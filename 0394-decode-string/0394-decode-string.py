class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        if len(s) == 1 and s[0].isnumeric():
            return ""
        for value in range(len(s)):
            if s[value] != "]":
                stack.append(s[value])
            else:
                sub = ""
                while stack[-1] != "[":
                    sub = stack.pop() + sub
                    print(sub)
                stack.pop()
                num = ""
                while stack and stack[-1].isnumeric():
                    num = stack.pop() + num
                stack.append(sub * int(num))
        return "".join(stack)