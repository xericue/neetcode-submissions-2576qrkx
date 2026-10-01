class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        indegrees = {}
        adj = {}

        for word in words:
            for char in word:
                adj[char] = set()
                indegrees[char] = 0 # we can build it AT THE SAME TIME!!!

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            
            for idx in range(min_len):
                if w1[idx] != w2[idx]:
                    # differing character
                    # if its already in, dont add it
                    if w2[idx] not in adj[w1[idx]]:
                        adj[w1[idx]].add(w2[idx])
                        indegrees[w2[idx]] += 1
                    break

        # sdkjhfjskdafhklsdahfsda

        ret_list = []
        q = collections.deque()
        for indeg in indegrees:
            if indegrees[indeg] == 0:
                q.append(indeg)

        while q:
            char = q.popleft()
            ret_list.append(char)

            for nei in adj[char]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)


        if len(ret_list) != len(indegrees):
            return ""

        return "".join(ret_list)