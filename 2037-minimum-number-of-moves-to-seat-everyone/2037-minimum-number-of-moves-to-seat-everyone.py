class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        ans=0
        for i in range(len(seats)):
            ans+=abs(sorted(seats)[i]-sorted(students)[i])
        return ans