class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        count_t = Counter(t)
        count_s = Counter(s)
        answer = 0

        for w , v in count_s.items():
            if w not in count_t:
                answer += v
            else:
                if v - count_t[w] > 0:
                    answer += (v - count_t[w])
                    
        return answer
                





