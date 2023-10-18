class Solution:
    def longestPalindrome(self, s: str) -> int:
       
        count = Counter(s)
        answer = 0
        count_odd = 0
        
        for k,v in count.items():
            if v % 2 == 0:
                answer += v
            elif v % 2 != 0 and v > 1:
                answer += v - 1
            if v % 2 != 0:
                count_odd += 1
                
        if count_odd > 0 :
            return answer + 1
        else:
            return answer
                