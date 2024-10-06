class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = defaultdict(lambda: defaultdict(int))

        def helper(w1, w2):
            if w1 in memo and w2 in memo[w1]:
                return memo[w1][w2]

            if w1 == w2:
                return 0
            elif w1 == "" and w2 == "":
                return 0
            elif w1 == "":
                return len(w2)
            elif w2 == "":
                return len(w1)

            result = 0
            if w1[-1] == w2[-1]:
                result = helper(w1[:-1], w2[:-1])
            else:
                result = min(helper(w1[:-1], w2[:-1]), helper(w1[:-1], w2), helper(w1, w2[:-1])) + 1

            memo[w1][w2] = result
            return result

        return helper(word1, word2)
