class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        max_value = max(arr)
        index = arr.index(max_value)
        if len(arr) > 2 and index != arr.index(arr[-1]) and index != arr.index(arr[0]): 
            def before(arr,index):
                before = arr[:index]
                for i in range(len(before)-1):
                    if before[i] >= before[i+1]:
                        return False
                return True
            def after(arr,index):
                after = arr[index:]
                after = after[::-1]
                for i in range(len(after)-1):
                    if after[i] >= after[i+1]:
                        return False
                return True

            return before(arr,index) and after(arr,index)
        
        
                    