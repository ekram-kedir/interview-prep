class Solution:
    def printVertically(self, s: str) -> List[str]:
        changedString = []
        answer = []

        strings = s.split()
        
        count_max = 0
        for s in strings:
            count = len(s)
            count_max = max(count,count_max)
        
        for s in strings:
            if len(s) < count_max:
                s = s + " " * (count_max - len(s))
                changedString.append(s)
            else:
                changedString.append(s)
       
        for s in zip(*changedString):
            answerWithString =  str("".join(s))
            answer.append(answerWithString.rstrip())
        return answer
        