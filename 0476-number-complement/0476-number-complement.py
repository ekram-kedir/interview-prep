class Solution:
    def findComplement(self, num: int) -> int:
        value = bin(num)
        new = ""
        for val in range(2,len(value)):
            if value[val] == "0":
                new += "1"
            else:
                new += "0"
        return int(new , 2)