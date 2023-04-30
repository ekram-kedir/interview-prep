class Solution:
    def racecar(self, target: int) -> int:
        
        visited = set([(0,1)])
        queue = deque([(0,1)])
        count = 0
        
        while queue:
            
            length = len(queue)
            count += 1
            
            for ele in range(length):
                position, speed = queue.popleft()
                
                if position == target:
                    return count - 1
                
                acc_position = position + speed
                acc_speed = speed * 2
                
                accelerate = (acc_position, acc_speed)
                if accelerate not in visited and 0 < acc_position < (target * 3):
                    queue.append(accelerate)
                    visited.add(accelerate)
                    
                if speed > 0: 
                    rev_speed = -1
                else:
                    rev_speed = 1
                rev_position = position
                reverse = (rev_position , rev_speed)
                
                if reverse not in visited:
                    queue.append(reverse)
                    visited.add(reverse)
        return -1