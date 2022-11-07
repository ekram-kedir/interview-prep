class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total=sum(cardPoints)
        t=z=sum(cardPoints[:(len(cardPoints)-k)])
        for i in range(k):
            z-=cardPoints[i]
            z+=cardPoints[i+(len(cardPoints)-k)]
            t=min(t,z)
        return total-t