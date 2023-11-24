class Solution:
    def generate(self, rowIndex: int) -> List[List[int]]:
        result = []
        def helper(rowIndex):
            if rowIndex == 0: 
                return [1]
            if rowIndex == 1: 
                return [1,1]
            ans = []
            before = helper(rowIndex - 1)
            before = [0] + before + [0]
            for i in range(len(before) - 1):
                ans.append((before[i] + before[i + 1]))
            return ans
        answer = []
        for i in range(rowIndex + 1):
            answer.append(helper(i))
        # print(answer)
        return answer[:-1]