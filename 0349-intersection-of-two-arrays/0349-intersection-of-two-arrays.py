class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # s1 = set(nums1)
        # s2 = set(nums2)
        # res = s1.intersection(s2)
        # return list(res)

        # Initialize seen dictionary and res array
        seen = {}
        result = []

        # mark values occurring in nums1
        for x in nums1:
          seen[x] = 1
          
        for x in nums2:
          # Check if x is in the dictionary and not in the result
          if seen.get(x, 0) == 1:
            result.append(x)
            seen[x] = 0

        # Return the result
        return result