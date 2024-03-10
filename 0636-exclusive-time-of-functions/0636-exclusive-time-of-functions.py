class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0 for i in range(n)]
        
        stack = []
        for log in logs:
            idx, tag, time = log.split(":")
            if tag == "start":
                stack.append((int(idx), int(time)))
            else:
                idx, startTime = stack.pop()
                curLen = int(time) - int(startTime) + 1
                res[idx] += curLen
                if stack:
                    prevIdx, prevTime = stack[-1]
                    res[prevIdx] -= curLen
        return res