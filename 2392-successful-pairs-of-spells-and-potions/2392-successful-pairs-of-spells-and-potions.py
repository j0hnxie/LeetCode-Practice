class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n, m = len(spells), len(potions)

        result = []
        for spell in spells:
            low, high = 0, m - 1
            while low < high:
                mid = low + (high - low) // 2
                if potions[mid] * spell >= success:
                    high = mid
                else:
                    low = mid + 1
            if potions[low] * spell >= success:
                result.append(m - low)
            else:
                result.append(0)

        return result