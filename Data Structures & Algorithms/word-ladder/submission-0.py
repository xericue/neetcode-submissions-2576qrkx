class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        total = 1
        # set up adj list for patterns
        adj = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                adj[pattern].append(word)
        
        # bfs
        visited = set([beginWord])
        q = collections.deque([beginWord])

        while q:
            n = len(q)
            # level order by patternized words
            for i in range(n):
                wrd = q.popleft()
                if wrd == endWord:
                    return total
                for j in range(len(wrd)):
                    pattern = wrd[:j] + "*" + wrd[j + 1:]
                    for nei in adj[pattern]:
                        # process all adjacent words
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            total += 1
                



        return 0