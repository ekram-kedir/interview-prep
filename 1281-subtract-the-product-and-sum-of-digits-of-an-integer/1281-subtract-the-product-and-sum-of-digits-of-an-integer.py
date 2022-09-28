class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product=1
        su=0
        for i in str(n):
            product*=int(i)
            su+=int(i)
        return product-su