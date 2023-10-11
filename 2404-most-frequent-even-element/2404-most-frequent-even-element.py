class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        answer = -inf
        ans = -inf
        array= []
        
        for k,v in count.items():
            if k % 2 == 0:
                answer = v
            ans = max(answer , ans)
            
        for k,v in count.items():
            if v == ans and k % 2 == 0:
                array.append(k)
        array.sort()
        
        return array[0] if ans != -inf else -1