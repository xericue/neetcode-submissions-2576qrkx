class TrieNode:
    def __init__(self):
        self.children = {}
        self.complete = False
    
    def insert(self, word):
        curr = self

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.complete = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        ret = set()
        path = set()

        for word in words:
            root.insert(word)
        
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in path or board[r][c] not in node.children):
                return

            path.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.complete:
                ret.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            path.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(ret)