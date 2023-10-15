class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        if n == 3:
            for i in range(3):
                if mountain_arr.get(i) == target:
                    return i
            return -1

        # First Search for the peak
        left, right = 0, n - 1
        peak = 0
        while left < right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) > mountain_arr.get(mid + 1):
                peak = mid
                right = mid
            else:
                left = mid + 1

        # Second Search in the left (increasing) part of the mountain
        low, high = 0, peak
        while low <= high:
            mid = low + (high - low) // 2
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            elif val < target:
                low = mid + 1
            else:
                high = mid - 1

        # Third Search in the right (decreasing) part of the mountain
        low, high = peak, n - 1
        while low <= high:
            mid = low + (high - low) // 2
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            elif val > target:
                low = mid + 1
            else:
                high = mid - 1

        return -1
