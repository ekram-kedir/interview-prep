class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        answer = ["0"] * len(s)
        count = s.count("1")
        if count == 1:
            answer[-1]  = "1"
        else:
            ptr = 0
            while count - 1 > 0:
                count -= 1
                answer[ptr] = "1"
                ptr += 1
            answer[-1]  = "1"
        return "".join(answer)