class TrieNode:
    def __init__(self, value = None, children = {}, is_word = False):
        self.value = value 
        self.children = {} # a set of Nodes
        self.is_word = is_word

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        if not word:
            return
        current = self.root

        for i in range(len(word)):
            if word[i] in current.children:
                current = current.children[word[i]] # get the node
                if i == len(word) - 1: # mark word as complete
                    current.is_word = True
            else:
                new_node = TrieNode(value = word[i])
                current.children[word[i]] = new_node
                current = new_node
                if i == len(word) - 1: # mark word as complete
                    current.is_word = True
        return 

    def search(self, word: str) -> bool:
        if not word:
            return False

        current = self.root
        for i in range(len(word)):
            cur = word[i]
            if cur in current.children:
                current = current.children[cur]

                if i == len(word) - 1: # termination check
                    return current.is_word

            else:
                return False
        
        return False    

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return False

        current = self.root
        for i in range(len(prefix)):
            cur = prefix[i]
            if cur in current.children:
                current = current.children[cur]
            else:
                return False
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)