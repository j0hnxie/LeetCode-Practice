class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglies = [0] * n
        uglies[0] = 1
        two_idx, three_idx, five_idx = 0, 0, 0
        next_two, next_three, next_five = 2, 3, 5

        for idx in range(1, n):
            cur_min = min([next_two, next_three, next_five])
            uglies[idx] = cur_min

            if cur_min == next_two:
                two_idx += 1
                next_two = 2 * uglies[two_idx]

            if cur_min == next_three:
                three_idx += 1
                next_three = 3 * uglies[three_idx]

            if cur_min == next_five:
                five_idx += 1
                next_five = 5 * uglies[five_idx]
        
        return uglies[-1]