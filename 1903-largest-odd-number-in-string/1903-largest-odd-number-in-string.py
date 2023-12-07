class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        change_to_list = list(num)
        max_odd = []
        
        for idx in range(len(change_to_list) - 1,-1 , -1):
            if int(change_to_list[idx]) % 2 != 0 and len(max_odd) == 0:
                max_odd = change_to_list[:idx + 1]
        return "".join(max_odd) if len(max_odd) != 0 else ""