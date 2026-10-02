class Node:
    def __init__(self):
        self.characters = {}
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        # either recursive; atvl traversing
        curr = self.root

        # maybe some outer node traversal here
        for character in word:
            if character not in curr.characters:
                curr.characters[character] = Node()
            curr = curr.characters[character]
        
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root

        for character in word:
            if character not in curr.characters:
                return False
            curr = curr.characters[character]
        
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for character in prefix:
            if character not in curr.characters:
                return False
            curr = curr.characters[character]
        return True