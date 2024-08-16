class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counts = [0] * 2
        for bill in bills:
            if bill == 5:
                counts[0] += 1
            elif bill == 10:
                if counts[0] <= 0:
                    return False
                counts[0] -= 1
                counts[1] += 1
            elif bill == 20:
                if counts[1] <= 0:
                    if counts[0] <= 2:
                        return False
                    else:
                        counts[0] -= 3
                else:
                    if counts[0] <= 0:
                        return False
                    else:
                        counts[0] -= 1
                        counts[1] -= 1
                    

            
        return True