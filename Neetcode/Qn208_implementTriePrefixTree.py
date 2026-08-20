class Node:

    def __init__(self, char = None, complete = False):
        self.children = {}
        self.char = char
        self.complete = complete

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        dummy = self.root

        for i in range(len(word)):
            char = word[i]

            if char not in dummy.children:
                dummy.children[char] = Node(char)
            
            dummy = dummy.children[char]
        
        dummy.complete = True
            
    def search(self, word: str) -> bool:
        dummy = self.root

        for i in range(len(word)):
            char = word[i]

            if char not in dummy.children:
                return False
        
            dummy = dummy.children[char]
        
        return dummy.complete

    def startsWith(self, prefix: str) -> bool:
        dummy = self.root

        for i in range(len(prefix)):
            char = prefix[i]

            if char not in dummy.children:
                return False
            
            dummy = dummy.children[char]
        
        return True
        
        