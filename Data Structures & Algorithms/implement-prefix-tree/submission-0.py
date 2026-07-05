class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_complete_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        # go character by character in the word, checking if the character
        # already exists
        
        for char in word:
            if char not in curr.children:
                # insert a new trie node for this newly discovered child
                curr.children[char] = TrieNode() # use the char as the key
            curr = curr.children[char] # update curr to progress, always
        
        # curr is now end of word
        curr.is_complete_word = True

    def search(self, word: str) -> bool:
        curr = self.root

        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        
        return curr.is_complete_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        
        for char in prefix: # the PREFIX BOY!!!
            if char not in curr.children:
                return False
            curr = curr.children[char]
        
        return True

        
        
        