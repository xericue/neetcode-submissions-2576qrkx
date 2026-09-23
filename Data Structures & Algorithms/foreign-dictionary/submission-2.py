class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # ground truths: adjacency list, kahn's algorithm, printing a string

        adj_list = {}
        indegrees = {}

        for word in words:
            for char in word:                    
                adj_list[char] = set()

        for char in adj_list:
            indegrees[char] = 0

        # hmm but i need to look at every word in relation to another
        for i in range(len(words) - 1):
            # i, i + 1
            word_one, word_two = words[i], words[i + 1]
            prefix_length = min(len(word_one), len(word_two))

            # prefix condition
            if len(word_one) > len(word_two) and word_one[:prefix_length] == word_two[:prefix_length]:
                return ""

            # find first differing character in a loop
            for idx in range(prefix_length):
                if word_one[idx] != word_two[idx]:
                    if word_two[idx] not in adj_list[word_one[idx]]:
                        adj_list[word_one[idx]].add(word_two[idx])
                        indegrees[word_two[idx]] += 1
                    break

        
        # kahns
        q = collections.deque()
        res = []

        for indeg in indegrees:
            if indegrees[indeg] == 0:
                q.append(indeg)
        
        while q:
            char = q.popleft()
            res.append(char)

            # kahns decrementing
            for nei in adj_list[char]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
        
        if len(res) != len(indegrees):
            return ""

        return "".join(res)