class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        def count_set_bits(num):
            count = 0
            while num:
                count += num & 1
                num >>= 1
            return count

        arr.sort(key=lambda x: (count_set_bits(x), x))

        return arr