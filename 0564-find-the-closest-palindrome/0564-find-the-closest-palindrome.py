class Solution:
    def duplicateHalf(self, half, isOdd):
        middle = ""
        half = str(half)
        if isOdd:
            middle = half[-1]
            half = half[:-1]
        
        reverse = half[::-1]
        result = half + middle + reverse
        return int(result)
            

    def nearestPalindromic(self, n: str) -> str:
        sz = len(n) # 4, 5
        mid = math.ceil(sz / 2)
        first_half = int(n[:mid])

        candidates = []
        candidates.append(self.duplicateHalf(first_half, sz % 2))
        candidates.append(self.duplicateHalf(first_half + 1, sz % 2))
        candidates.append(self.duplicateHalf(first_half - 1, sz % 2))
        candidates.append(10 ** (sz - 1) - 1)
        candidates.append(10 ** sz + 1)

        print(candidates)
        diff, result = float('inf'), ""
        current = int(n)

        for candidate in candidates:
            if candidate == current:
                continue

            if abs(candidate - current) < diff:
                diff = abs(candidate - current)
                result = candidate
            elif abs(candidate - current) == diff:
                result = min(result, candidate)
        return str(result)