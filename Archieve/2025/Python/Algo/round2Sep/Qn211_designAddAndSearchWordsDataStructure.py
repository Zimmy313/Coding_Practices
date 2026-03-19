class TreeNode:
    def __init__(self, val = None, children=None, is_word = False):
        self.val = val
        self.children = {} if children is None else children
        self.is_word = is_word

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = TreeNode(val = ch)
            current = current.children[ch]
        current.is_word = True


    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.is_word
            
            ch = word[i]
            if ch == '.':
                for child in node.children.values():
                    if dfs(child, i+1):
                        return True
                return False
            else:
                if ch not in node.children:
                    return False
                return dfs(node.children[ch], i+1)

        return dfs(self.root, 0)
                
                

        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)