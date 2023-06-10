class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        
        mon_stack = [len(arr) - 1]
        recordIdx = inf
        recordVal = inf
        for i in range(len(arr) - 2 , -1 , -1):
            if arr[mon_stack[-1]] >= arr[i]:
                mon_stack.append(i)
                if len(mon_stack) == len(arr):
                    return arr
            else:
                for j in range(len(mon_stack) - 1 , -1 , -1):
                    if arr[mon_stack[j]] < arr[i]:
                        if recordIdx != inf and arr[recordIdx] == arr[mon_stack[j]]:
                            continue
                        recordIdx = mon_stack[j]
                arr[i] , arr[recordIdx] = arr[recordIdx] , arr[i]
                break
        
        return arr
                