class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ans  = []
        res  = []
        
        for i in zip(heights,names):
            
            ans.append(i)
            ans.sort(reverse=True)

        for a,b in ans:
            
            res.append(b)
            
        return res