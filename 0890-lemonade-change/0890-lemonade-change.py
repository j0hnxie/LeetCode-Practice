class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                if fives == 0:
                    return False
                fives -= 1
                tens += 1
            elif bill == 20:
                if tens == 0:
                    if fives <= 2:
                        return False
                    else:
                        fives -= 3
                else:
                    if fives == 0:
                        return False
                    else:
                        fives -= 1
                        tens -= 1
                        
        return True