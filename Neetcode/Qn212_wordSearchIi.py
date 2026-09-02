class Node:
    def __init__(self, char, index = None,isWord = False):
        self.char = char
        self.children = {}
        self.index = index
        self.isWord = isWord

class Trie:
    def __init__(self, row, col, board, words):
        self.root = Node(None)
        self.row = row
        self.col = col
        self.res = []
        self.board = board
        self.words = words

    def addWord(self, word, index):
        dummy = self.root

        for i in range(len(word)):
            char = word[i]

            if char not in dummy.children:
                child = Node(char = char)
                dummy.children[char] = child
            
            dummy = dummy.children[char]

        dummy.isWord = True
        dummy.index = index
    
    def search(self, node, i, j):
        moves = [(1,0), (0,1), (-1,0), (0,-1)]
        char = self.board[i][j]
        self.board[i][j] = "#"

        if char in node.children:
            nnode = node.children[char]

            if nnode.isWord and nnode.index is not None:
                self.res.append(self.words[nnode.index])
                nnode.index = None

            for di, dj in moves:
                ni, nj = i + di, j + dj

                if 0 <= ni < self.row and 0 <= nj < self.col and self.board[ni][nj] != "#":
                    self.search(nnode, ni, nj)
        self.board[i][j] = char

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        row, col = len(board), len(board[0])
        trie = Trie(row, col, board, words)

        for i, word in enumerate(words):
            trie.addWord(word, i)
        
        for i in range(row):
            for j in range(col):
                dummy = trie.root

                trie.search(dummy, i, j)
        
        return trie.res


