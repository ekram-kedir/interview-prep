class Solution:
    def isPalindrome(self, s: str) -> bool:
        palin = ""
        for i in s:
            if i.isalpha():
                palin += i.lower()
            if i.isnumeric():
                palin += i
        left = 0
        right = len(palin)-1
        while left <= right:
            if palin[left] != palin[right]:
                return False
            left += 1
            right -= 1
        return True
        

        
