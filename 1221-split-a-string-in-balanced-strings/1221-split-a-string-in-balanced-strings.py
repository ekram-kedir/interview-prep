class Solution:
    def balancedStringSplit(self, s: str) -> int:
        total = 0
        countR = 0
        countL = 0
        
        for alph in s:
            if alph == "R":
                countR += 1
            elif alph == "L":
                countL += 1
            if countR == countL:
                total += 1
                countR = countL = 0
        return total