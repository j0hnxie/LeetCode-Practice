class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        n = len(nums)

        mono = deque()
        max_num = max(nums[:k])
        for idx in range(k):
            while mono and nums[mono[-1]] <= nums[idx]:
                mono.pop()
            mono.append(idx)
        res.append(nums[mono[0]])

        for end in range(k, n):
            while mono and nums[mono[-1]] <= nums[end]:
                mono.pop()

            mono.append(end)

            while mono[0] <= end - k:
                mono.popleft()
            res.append(nums[mono[0]])
            # print(mono)
        # res.append(nums[mono[0]])
        return res