class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []
        for idx, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                cur_index = stack.pop()
                answer[cur_index] = idx - cur_index
            stack.append(idx)
        return answer
