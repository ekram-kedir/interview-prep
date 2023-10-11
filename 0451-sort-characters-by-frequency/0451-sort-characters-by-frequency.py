class Solution:
    def frequencySort(self, s: str) -> str:
        
        answer = ""
        count = (Counter(s))
        updated = sorted(count.items() , key = lambda x:x[1])
        
        for k,v in updated:
            answer += k * (v)
        return answer[::-1]