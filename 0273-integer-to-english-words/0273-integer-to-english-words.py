class Solution:
    def numberToWords(self, num: int) -> str:
        suffixes = ["", "Thousand", "Million", "Billion"]

        mapping = {
            0: "Zero",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
        }

        print("finished mapping")
        def convertLessThanThousand(num):
            print("called")
            res = ""
            if len(num) == 3:
                hundreds = int(num[0])
                if hundreds:
                    res += " " + mapping[hundreds] + " Hundred"
                num = num[1:]
            if len(num) <= 2:
                num_int = int(num)
                if not num_int:
                    return res
                elif num_int in mapping:
                    res += " " + mapping[num_int]
                else:
                    tens = int(num[0])
                    tens *= 10
                    res += " " + mapping[tens]
                    ones = int(num[1])
                    res += " " + mapping[ones]
            return res                
        
        num_str = str(num)
        stack = []
        cur = ""
        for char in reversed(num_str):
            cur = char + cur
            if len(cur) == 3:
                stack.append(cur)
                cur = ""
        if cur:
            stack.append(cur)
        
        res = ""
        counter = 0
        for current_group in stack:
            print(res)
            # current_group = stack.pop()
            group_str = convertLessThanThousand(current_group)
            print(group_str)
            group_str += " " + suffixes[counter] if group_str else ""
            print(group_str)
            res = group_str + res
            print(res)
            counter += 1
            print(res)

        res = res.strip()
        return res if res else "Zero"