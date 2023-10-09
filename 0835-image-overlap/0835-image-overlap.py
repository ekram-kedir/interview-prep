class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        def get_bit(nums):
            value = 0
            for i in range(n):
                if nums[i]:
                    value ^= 1 << i
            
            return value
        
        def count_similar(nums1,nums2):
            count = 0
            for i in range(n):
                bit = 1 << i
                if (nums1 & bit) and (nums2 & bit):
                    count += 1
            
            return count
        
        def right(nums):
            new_n = deepcopy(list(nums))
            for i in range(n):

                if new_n[i] & 1 <<(n-1):
                    new_n[i] ^= (1 <<(n-1))

                new_n[i] <<= 1
            
            return tuple(new_n)
        
        def left(nums):
            new_n = deepcopy(list(nums))
            for i in range(n):

                if new_n[i] & 1 :
                    new_n[i] ^= 1

                new_n[i] >>= 1
            
            return tuple(new_n)
    
        def up(nums):
            new_n = deepcopy(list(nums))
            return tuple([0]+ list(new_n[:n-1]))
        
        def down(nums):
            new_n = deepcopy(list(nums))
            return tuple(list(new_n[1:]) + [0])
            
        
      
            
        
        img1_row,img2_row = [],[]
        for i in range(n):
            img1_row.append(get_bit(img1[i]))
            img2_row.append(get_bit(img2[i]))
        
        dic = {"up":up, "down":down,"left":left, "right":right}
        
        @cache
        def dfs(img1_row, move1,move2):
            
            if sum(img1_row) == 0:
                return 0
            
            cur_count = 0
            for i in range(n):
                cur_count += count_similar(img1_row[i],img2_row[i])
            
            
            
            
            up_count = dfs(dic[move1](img1_row),move1, move2)
            down_count = dfs(dic[move2](img1_row),move1,move2)
            return max(cur_count, up_count, down_count)
    
        
        a = -inf
        
        a = max(a,dfs(tuple(img1_row), "up","left"))
        a = max(a,dfs(tuple(img1_row), "up","right"))
        a = max(a,dfs(tuple(img1_row), "down","left"))
        a = max(a,dfs(tuple(img1_row), "down","right"))
        
        return a

            
                
        
            
        
                    
            