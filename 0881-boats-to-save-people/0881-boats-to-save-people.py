class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        people.sort()
        
        left ,right = 0,len(people)-1
        
        while left <= right:
            dif = limit-people[right]
            right -= 1
            ans += 1
            if dif >= people[left]:
                left += 1
        return ans
                