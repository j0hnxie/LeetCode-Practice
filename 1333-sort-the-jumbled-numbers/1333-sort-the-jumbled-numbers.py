class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        together = []
        for idx, num in enumerate(nums):
            num_str = str(num)
            new_num = 0
            for char in num_str:
                new_digit = mapping[int(char)]
                new_num = new_num * 10 + new_digit
            together.append((new_num, idx))
        together = sorted(together)
        res = [nums[pair[1]] for pair in together]
        return res