class Solution:
    def intToRoman(self, num: int) -> str:
        values = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
        }
        multiplier = 1
        cur = num
        res = ""
        while multiplier <= num:
            # print(cur)
            cur_dig = cur % 10
            cur_val = cur_dig * multiplier
            if cur_dig == 9:
                res = values[multiplier] + values[cur_val + multiplier] + res
            elif cur_dig >= 5:
                res = values[5 * multiplier] + (cur_dig - 5) * values[multiplier] + res
            elif cur_dig == 4:
                res = values[multiplier] + values[5 * multiplier] + res
            else:
                res = cur_dig * values[multiplier] + res
            cur = int(cur / 10)
            multiplier *= 10
        return res
        
        