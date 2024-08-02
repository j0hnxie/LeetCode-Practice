class Solution:
    def candy(self, ratings: List[int]) -> int:
        up, down, peak = 0, 0, 0
        prev_rating = float('-inf')
        res = 0
        candies = []

        for rating in ratings:
            if rating > prev_rating:
                up += 1
                down = 0
                peak = up
                res += up
            elif rating < prev_rating:
                down += 1
                up = 1
                res += down + (1 if peak <= down else 0)
            else:
                up, down = 1, 0
                peak = 1
                res += 1
            prev_rating = rating
        return res