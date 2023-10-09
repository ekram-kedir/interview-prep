class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        map_val = collections.defaultdict(int)
        ones_img1 = []
        ones_img2 = []
        length = len(img1)
        
        for indx1 in range(length):
            for indx2 in range(length):
                if img1[indx1][indx2] == 1:
                    ones_img1.append((indx1 , indx2))
                if img2[indx1][indx2] == 1:
                    ones_img2.append((indx1 , indx2))
        answer = 0
        for first in ones_img1:
            for second in ones_img2:
                map_val[(second[0] - first[0] , second[1] - first[1])] += 1
                answer = max(answer , map_val[(second[0] - first[0] , second[1] - first[1])])
        return answer