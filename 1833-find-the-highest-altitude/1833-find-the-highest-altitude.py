class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        cur = 0

        for num in gain:
            cur += num
            highest = max(highest, cur)

        return highest