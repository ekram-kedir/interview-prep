class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
            total = 0
            tens = 0
            fives = 0
            twenys = 0
            for i in range(len(bills)):
                if bills[i] == 5:
                    total += 5
                    fives += 1
                elif bills[i] == 10 and total >= 5 and fives >= 1:
                    total += 5
                    tens += 1
                    fives -= 1
                elif bills[i] == 10 and ((total < 5) or (fives < 1)):
                    return False
                elif bills[i] == 20 and total >= 15 and tens > 0 and fives >= 1:
                    total -= 15
                    tens -= 1
                    fives -= 1
                elif bills[i] == 20 and total >= 15 and tens == 0 and fives >= 3:
                    total -= 15
                    fives -= 3
                elif bills[i] == 20 and fives == 0:
                    return False
                elif bills[i] == 20 and (total < 15) or ((tens == 0) and (fives < 3)):
                    return False
                elif bills[i] == 20 and total < 15 and tens > 0 and fives < 1:
                    return False
            return True