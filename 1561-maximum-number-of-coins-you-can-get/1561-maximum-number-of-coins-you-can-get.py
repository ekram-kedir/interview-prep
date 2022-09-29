class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        su=0
        piles.sort(reverse=True)
        for i in range(1,len(piles)-int(len(piles)/3),2):
            su+=piles[i]
        return su