class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        maxval=0
        while r<len(prices):
            if prices[l]<prices[r]:
                dif=prices[r]-prices[l]
                maxval=max(maxval,dif)
            else:
                l=r
            r+=1
        return maxval