class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """
        if len(words) < 2:
            return words[0]

        adj list collections.defaultdict(list)
        
        in degrees
        # no visited set is necessary i think? handled by indegrees

        # building the adjacency list
        l, r = 0, 1
        while r < len(words):
            left = words[l]
            right = words[r]
            idx = 0
            while idx < len(left) and idx < len(right):

                idx += 1

            l += 1
            r += 1

        queue for kahns

        while queue
            pop new node

            for nei in adj[node]
                indegrees[nei] -= 1
                if indegrees[nei] == 0
                    append to queue
        """

        # adjacency list
        adj = {}
        for word in words:
            for char in word:
                adj[char] = set()
        
        # indegrees
        indegrees = {char: 0 for char in adj}

        # build adjacency list
        l, r = 0, 1
        while r < len(words):
            left = words[l]
            right = words[r]
            min_len = min(len(left), len(right))
            if len(left) > len(right) and left[:min_len] == right[:min_len]:
                return "" # prefixes are the same, left word up until minlen
            
            # otherwise, find the first differing character
            for idx in range(min_len):
                if left[idx] != right[idx]:
                    # catch duplicates: if the left word doesnt already
                    # have a directed edge to the mismatched character,
                    # add it
                    if right[idx] not in adj[left[idx]]: 
                        adj[left[idx]].add(right[idx])
                        # update indegree of this mismatched character
                        indegrees[right[idx]] += 1
                    break # since we found it, move on

            l += 1
            r += 1

        # start kahns queue
        q = collections.deque()
        for indeg in indegrees:
            if indegrees[indeg] == 0:
                q.append(indeg)

        res = []

        # kahns
        while q:
            char = q.popleft()
            res.append(char)

            # regular kahns
            for nei in adj[char]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
            
        # if the res doesnt match how many edges there should be
        if len(res) != len(indegrees):
            return ""

        return "".join(res)
