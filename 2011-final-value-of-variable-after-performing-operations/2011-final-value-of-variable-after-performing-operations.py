class Solution:
    def finalValueAfterOperations(self, ops: List[str]) -> int:
        x = 0
        for i in range(len(ops)):
            if (ops[i] == "--X") or (ops[i] == "X--"):
                x -= 1
            elif (ops[i] == "++X") or (ops[i] == "X++"):
                x += 1
        return x