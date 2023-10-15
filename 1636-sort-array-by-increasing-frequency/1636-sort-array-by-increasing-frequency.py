class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        dic = Counter(nums)
        updated = sorted(dic.items() , key = lambda x:(x[1] , -x[0]))
        res = []
        for k,v in updated:
            while v > 0:
                res.append(k)
                v -= 1
        return res