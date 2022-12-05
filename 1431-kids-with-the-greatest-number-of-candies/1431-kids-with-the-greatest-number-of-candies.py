class Solution:
    def kidsWithCandies(self, candies: List[int], extracandies: int) -> List[bool]:
        high = max(candies)
        ans = []
        for i in range(len(candies)):
            if candies[i] + extracandies >= high:
                ans.append(True)
            else:
                ans.append(False)
        return ans