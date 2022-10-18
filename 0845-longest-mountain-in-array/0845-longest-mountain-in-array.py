class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        count=0
        begn,end=0,1
        while begn<len(arr):
            while begn<len(arr)-1 and arr[begn]>=arr[begn+1]:
                begn+=1
            end=begn+1
            while end<len(arr)-1 and arr[end]<arr[end+1]:
                end+=1
            while end<len(arr)-1 and arr[end]>arr[end+1]:
                end+=1
                count=max(count,end-begn+1)
            begn=end
        return count
            