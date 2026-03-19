from typing import *

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
        
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def isUniform(x0,y0, size): # checking for uniformity
            val = grid[x0][y0]
            for i in range(x0,x0+size):
                for j in range(y0,y0+size):
                    if grid[i][j] != val:
                        return False
            return True
        
        def build(x0,y0, size):
            if isUniform(x0,y0,size):
                return Node(val=bool(grid[x0][y0]), isLeaf=True)

            half = size//2
            return Node(
                val=True,
                isLeaf=False,
                topLeft=build(x0,y0,half),
                topRight=build(x0,y0+half,half),
                bottomLeft=build(x0+half,y0, half),
                bottomRight=build(x0+half,y0+half,half)
            )
        return build(0,0,len(grid))