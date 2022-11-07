class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        inc=[0]
        dec=[0]
        
        for i,j in zip(security,security[1:]):
            if i>j:
                dec.append(dec[-1]+1)
            elif i<j:
                dec.append(0)
            else:
                dec.append(dec[-1]+1)
        security=security[::-1]
        for i,j in zip(security,security[1:]):
            if i>j:
                inc.append(inc[-1]+1)
            elif i<j:
                inc.append(0)
            else:
                inc.append(inc[-1]+1)
        inc.reverse()
        
        ans=[]
        for i in range(len(security)):
            if i>=time and i+time<len(security) and inc[i]>=time and dec[i]>=time:
                ans.append(i)
        return ans