class Solution:
    def findDuplicate(self, arr: List[int]) -> int:
        pointer = 0
        length = len(arr)
        
        while pointer < length:
            reference = arr[pointer]
            if (arr[pointer] != pointer + 1)  and arr[pointer] == arr[reference - 1]:
                pointer += 1
            elif arr[pointer] != pointer + 1:
                arr[pointer] , arr[reference - 1] = arr[reference - 1] , arr[pointer]
            else:
                pointer += 1
        for num in range(len(arr)):
            if arr[num] != num + 1:
                return arr[num]
        
        