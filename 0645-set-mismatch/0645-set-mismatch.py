class Solution:
    def findErrorNums(self, arr: List[int]) -> List[int]:
        
        pointer = 0
        length = len(arr)
        answer = []
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
                answer.append(arr[num])
                answer.append(num + 1)
        return  answer
        
        
        