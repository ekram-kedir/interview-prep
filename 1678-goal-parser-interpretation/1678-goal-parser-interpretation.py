class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        for i in range(len(command)):
            if command[i] == "G":
                ans += command[i]
            elif command[i] == ")" and command[i-1] == "(":
                ans += "o"
            elif command[i] == "a" and command[i-1] == "(":
                ans += "al"
        return ans
    