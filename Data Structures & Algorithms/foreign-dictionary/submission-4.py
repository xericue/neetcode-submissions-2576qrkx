class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # graph problem

        adj_list = {}
        indegrees = {}

        # populate adj_list using characters
        for word in words:
            for char in word:
                adj_list[char] = set()

        # populate indegrees using characters
        for char in adj_list:
            indegrees[char] = 0

        # OKAY POPULATE THE ADJACENCY LIST HERE WE GO
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))

            # 0. prefix condition
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            
            # 1. iterate through min_len, breaking at a differing character
            for idx in range(min_len):
                if w1[idx] != w2[idx]:
                    # can we add it to our adj_list?
                    if w2[idx] not in adj_list[w1[idx]]:
                        adj_list[w1[idx]].add(w2[idx])
                        indegrees[w2[idx]] += 1
                    break

        q = collections.deque()
        resulting_arr = []    # because we want to use it for comparison with the amount of edges
                              # later; also, it's an easy operation to join it together at the end!
        # populate queue - regular kahns
        for indeg in indegrees:
            if indegrees[indeg] == 0:
                q.append(indeg)

        while q:
            char = q.popleft()
            resulting_arr.append(char)

            # neighbors
            for nei in adj_list[char]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)

        # check if it was possible to construct a full word/we exhausted all edges
        if len(resulting_arr) != len(indegrees):
            return ""

        return "".join(resulting_arr)