class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [(-1, -1)]
        result = 0
        
        for idx, height in enumerate(heights):
            while stack and stack[-1][0] >= height:
                cur_height, cur_idx = stack.pop()
                length = idx - stack[-1][1] - 1
                result = max(result, length * cur_height)
            stack.append((height, idx))
            
        return result
        
#         # 0s
#         n = len(heights)
#         heights = deque(heights)
#         heights.appendleft(0)
#         heights.append(0)
        
#         # variables
#         stack = []
#         result = 0
#         prev_small = [0] * (n + 2)
#         next_small = [n + 1] * (n + 2)
        
#         # forward
#         for idx, height in enumerate(heights):
#             # increasing
#             while stack and stack[-1][0] > height:
#                 cur_height, cur_idx = stack.pop()
#             if idx != 0:
#                 prev_small[idx] = stack[-1][1]
#             stack.append((height, idx))
            
#         # backward
#         stack = []
#         for idx in range(n + 1, -1, -1):
#             height = heights[idx]
#             # increasing
#             while stack and stack[-1][0] > height:
#                 cur_height, cur_idx = stack.pop()
#                 length = cur_idx - idx
#                 result = max(result, length * cur_height)
#             if idx != n + 1:
#                 next_small[idx] = stack[-1][1]
#             stack.append((height, idx))
            
#         print(next_small)
#         print(prev_small)
        
#         for idx in range(n + 2):
#             length = next_small[idx] - prev_small[idx] - 1
#             height = heights[idx]
#             result = max(result, length * height)
            
#         return result
        