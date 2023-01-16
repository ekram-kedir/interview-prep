class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        k = []
        ans = []
        an = ""
        
        for i in zip(*strs):
            ans .append(i)
        for i in range(len(ans)):
            an = "".join(map(str,ans[i]))
            k.append(an)
        for i in range(len(k)):
            sorted_one ="".join(map(str,sorted(k[i])))
            if k[i] != sorted_one:
                count += 1
        return count
                
                