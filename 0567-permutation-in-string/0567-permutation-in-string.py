class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        window = []
        count_s1 = Counter(s1)
        k = len(s1)
        n = len(s2)
        if k > n:
            return 
        for alph in range(k):
            window.append(s2[alph])
        if count_s1 == Counter(window):
            return True
    
        count = 0
        for alph in range(k , n):
            window.pop(0)
            window.append(s2[alph])
            if count_s1 == Counter(window):
                count+=1
        if count != 0:
            return True
        return False
           
        