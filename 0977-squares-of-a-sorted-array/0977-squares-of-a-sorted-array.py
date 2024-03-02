class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = 0
        r = n - 1
        mid = l
        
        while l < r:
            mid = l + (r - l) // 2
            # print(mid)
            
            if nums[mid] < 0:
                l = mid + 1
            elif nums[mid] > 0:
                r = mid
            else:
                break
        
        res = []
        if nums[mid] > 0:
            l = mid - 1
            r = mid
        elif nums[mid] < 0:
            l = mid
            r = mid + 1
        else:
            res.append(0)
            l = mid - 1
            r = mid + 1
            
        # print(mid)
        # print(l)
        # print(r)
            
        while l >= 0 or r < n:
            if l < -1:
                res.append(nums[r] * nums[r])
                r += 1
                continue
            if r >= n:
                res.append(nums[l] * nums[l])
                l -= 1
                continue
            
            if abs(nums[l]) < nums[r]:
                res.append(nums[l] * nums[l])
                l -= 1
            else:
                res.append(nums[r] * nums[r])
                r += 1
        return res
            