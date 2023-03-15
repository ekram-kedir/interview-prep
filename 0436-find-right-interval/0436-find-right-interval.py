class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        front = []
        back = []
        ans = [-1] * len(intervals)
        
        for interval in intervals:
            front.append(interval[0])
            back.append(interval[1])
    
        frontSort = sorted(front)
        
        for val in range(len(back)):

            left = -1
            right = len(front)

            while left + 1 < right:
                mid = left + (right - left)//2
                if back[val] > frontSort[mid]:
                    left = mid
                else:
                    right = mid
           
            if right == len(front):
                continue
            else:
                ans[val] = front.index(frontSort[right])
        return ans
            