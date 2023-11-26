class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @cache
        def collatz_count(num):
            if num == 1:
                return 0
            elif num % 2 == 0:
                return 1 + collatz_count(num // 2)
            else:
                return 1 + collatz_count(3 * num + 1)

        elements = list(range(lo, hi + 1))
        elements.sort(key=collatz_count)
        return elements[k - 1]
