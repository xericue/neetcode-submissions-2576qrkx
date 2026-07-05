class TrieNode:
    def __init__(self):
        self.children = {}
        self.complete = False

class WordDictionary:
    # mmm so this is just asking for a trie with metacharacters
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                # add a new node for the character
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        
        curr.complete = True

    def search(self, word: str) -> bool:
        # dfs on a tree
        # ...UHHH...

        def dfs(j, node): # j is index parameter
            curr = node
            
            for i in range(j, len(word)): # our index parameter since
            # we're going forward (example, ".ad" wouldnt start at .
            # every time)
                char = word[i]

                if char == ".":
                    # recursive backtracking here
                    for child in curr.children.values(): # why values?
                        if dfs(i + 1, child):
                            return True # already found a matching path
                    return False # otherwise
                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            
            return curr.complete

        return dfs(0, self.root) # 0 for index 0/beginning of word
        # and start @ root node of trie
