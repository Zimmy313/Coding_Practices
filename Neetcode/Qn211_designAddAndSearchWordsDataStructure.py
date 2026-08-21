class Node:

    def __init__(self, val = None, isWord = False):
        self.children = {}
        self.val = val
        self.isWord = isWord

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        dummy = self.root

        for char in word:
            if char not in dummy.children:
                dummy.children[char] = Node(char)
            
            dummy = dummy.children[char]
        
        dummy.isWord = True
        

    def search(self, word: str) -> bool:

        # # this involves list slicing which is inefficient. work with index directly
        # def helper(word, node):
        #     dummy = node

        #     for i, char in enumerate(word):
        #         if char == ".":
        #             for child in dummy.children.values():
        #                 result = helper(word[i+1:], child) # here is additional overhead
        #                 if result == True:
        #                     return result
        #             return False
        #         elif char in dummy.children:
        #             dummy = dummy.children[char]
        #         else:
        #             return False
            
        #     return dummy.isWord

        # return helper(word, self.root)

        def helper(i, node):
            if i == len(word):
                return node.isWord

            char = word[i]

            if char == ".":
                for child in node.children.values():
                    if helper(i + 1, child):
                        return True
                return False
            
            if char not in node.children:
                return False
            
            return helper(i+1, node.children[char])
        
        return helper(0,self.root)