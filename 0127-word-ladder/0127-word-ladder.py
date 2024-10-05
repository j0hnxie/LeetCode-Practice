class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList + [beginWord])
        wordList = list(wordList)

        n, m = len(wordList), len(beginWord)
        adj_list = defaultdict(list)

        for idx in range(n):
            curWord = wordList[idx]
            for charIdx in range(m):
                tempWord = curWord[:charIdx] + "*" + curWord[charIdx + 1:]
                adj_list[tempWord].append(curWord)

        queue = deque([beginWord])
        visited = set([beginWord])

        dist = 1
        while queue:
            sz = len(queue)
            for _ in range(sz):
                cur = queue.popleft()
                
                if cur == endWord:
                    return dist

                for charIdx in range(m):
                    tempWord = cur[:charIdx] + "*" + cur[charIdx + 1:]
                    for neighbor in adj_list[tempWord]:
                        if neighbor in visited:
                            continue
                        
                        visited.add(neighbor)
                        queue.append(neighbor)

            dist += 1

        return 0