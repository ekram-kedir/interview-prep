class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        answer = defaultdict(int)
        for element in range(lo, hi + 1):
            answer[element] = 0
            num = element
            count = 0
            while element != 1:
                
                if element % 2 == 0:
                    element = element / 2
                else:
                    element = element * 3 + 1
                count += 1
            answer[num] = count
        updated = sorted(answer.items(), key = lambda x:x[1])
        return updated[k - 1][0]
        
                