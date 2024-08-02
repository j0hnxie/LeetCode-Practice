class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cust_comp(a, b):
            if int(a + b) > int(b + a):
                return -1
            elif int(a + b) < int(b + a):
                return 1
            else:
                return 0

        nums = [str(num) for num in nums]
        nums = sorted(nums, key=functools.cmp_to_key(cust_comp))
        print(nums)
        
        return str(int("".join(nums)))