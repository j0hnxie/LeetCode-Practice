class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        def dfs(word, length):
            if word in memo:
                return memo[word]
            elif word not in word_lengths[length]:
                return 0

            n = len(word)
            res = 0
            for idx in range(n):
                smaller_word = word[:idx] + word[idx + 1:]
                if smaller_word in word_lengths[length - 1]:
                    res = max(res, dfs(smaller_word, length - 1))
            res += 1
            memo[word] = res
            return memo[word]

        word_lengths = defaultdict(set)
        lengths = set()
        largest = 0
        
        for word in words:
            n = len(word)
            lengths.add(n)
            largest = max(largest, n)
            word_lengths[n].add(word)
        
        lengths = sorted(list(lengths), reverse = True)

        memo = defaultdict(int)

        res = 0
        for length in lengths:
            for word in word_lengths[length]:
                if word not in memo:
                    res = max(res, dfs(word, length))
        
        return res


        # first = True
        # for length in lengths:
        #     if first:
        #         for word in wordLengths[length]:
        #             memo[word] = 1
        #     else:
        #         for word in wordLengths[length]:
        #             if
