class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre = 1
        pres = []
        for num in nums:
            if num == 0:
                pres.append(0)
                pre = 1
            else:
                pre *= num
                pres.append(pre)

        first_neg = -1
        res = float('-inf')
        for idx, pre in enumerate(pres):

            res = max(res, pre)
            if first_neg != -1:
                res = max(res, pre / pres[first_neg])

            if pre < 0 and first_neg == -1:
                first_neg = idx
            elif pre == 0:
                first_neg = -1
            
        
        # print(pres)
        # print(res)
        # return 0
        return int(res)
