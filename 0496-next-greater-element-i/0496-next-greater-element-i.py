class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answerStack = []
        answerDict = defaultdict(int)
        answer = []
        for num in nums2:
            while answerStack and num > answerStack[-1]:
                answerDict[answerStack.pop()] = num
            answerStack.append(num)

        for ans in nums1:
            if ans not in answerDict.keys():
                answer.append(-1)
            else:
                answer.append(answerDict[ans])
            
        return answer