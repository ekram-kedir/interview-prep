class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score=0
        max_score=0
        tokens=sorted(tokens)
        l,r=0,len(tokens)-1
        while l<=r:
            if power>= tokens[l]:
                power-=tokens[l]
                score+=1
                max_score=max(score,max_score)
                l+=1
            elif score>0:
                power+=tokens[r]
                r-=1
                score-=1
            else:
                break
        return max_score
                
            
            