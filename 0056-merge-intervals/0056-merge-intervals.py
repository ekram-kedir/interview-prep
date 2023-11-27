class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        identify_intervals = []
        
        for start, end in intervals:
            identify_intervals.append([start, 0])
            identify_intervals.append([end, 1])
        
        identify_intervals.sort()
        
        merged_intervals = []
        start = 0
        count = 0
        
        for point, value in identify_intervals:
            if count == 0 and value == 0:
                start = point
            count += 1 if value == 0 else -1

            if count == 0:
                merged_intervals.append([start, point])

        return merged_intervals
