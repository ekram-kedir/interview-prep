class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        result = []
        answer = 0
        skill.sort()
        for i in range(len(skill)):
            result.append(skill[i] + skill[-i - 1])
            answer += skill[i] * skill[-i - 1]
        if len(set(result)) == 1:
            return answer//2
        else:
            return -1