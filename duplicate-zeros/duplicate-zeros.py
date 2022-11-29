class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        p = 0
        while p < len(arr):
            if arr[p] == 0:
                if p == len(arr) - 1:
                      pass
                arr.pop()
                arr.insert(p + 1 , 0)
                p += 2
            else:
                p += 1
      
           
    