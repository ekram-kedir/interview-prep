class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        modCount ={0:1}
        res = 0
        prefix = 0
        
        for num in nums:
            prefix = (prefix + num) % k
            res += modCount.get(prefix,0)
            modCount[prefix] =1+modCount.get(prefix,0)
        
        return res
      