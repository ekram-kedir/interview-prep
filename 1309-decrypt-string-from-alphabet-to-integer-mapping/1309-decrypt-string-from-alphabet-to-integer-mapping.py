class Solution:
    def freqAlphabets(self, s: str) -> str:
        init = 96 
        pointer = 0
        result = ""
        while pointer < len(s):
            if pointer + 2 < len(s) and s[pointer + 2] == "#":
                result += chr(init + int(s[pointer : pointer + 2]))
                pointer += 3
                
            else:
                
                result += chr(init + int(s[pointer]))
                pointer += 1
        return result