class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and len(trust) == 0:
            return 1

        trustOthers = set()
        
        trusted = {}
        
        for trus in trust:
            trustOthers.add(trus[0])
            trusted[trus[1]] = trusted.get(trus[1], 0) + 1
        
        for key, value in trusted.items():
            if value == n - 1 and key not in trustOthers:
                return key
        return -1