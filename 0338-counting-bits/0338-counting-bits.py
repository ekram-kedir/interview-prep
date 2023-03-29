class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for num in range(n + 1):
            value = bin(num)
            ans.append(str(value).count("1"))
        return ans