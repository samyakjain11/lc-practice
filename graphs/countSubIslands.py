from typing import *

# class Solution:
def countSubIslands(grid1: List[List[int]], grid2: List[List[int]]) -> int:
    # naive solution: find list of islands on both grid1 and grid2
    # optimized: find list of islands on grid 2 only and then check if those islands are filled on grid1, time: O(m*n) + O(m*n)*O(1)
    grid2_islands = []
    num_subislands = 0

    def searchIsland(x,y, island_area):
        if x < 0 or x >= len(grid2) or y < 0 or y >= len(grid2[0]):
            return
        if grid2[x][y] != 1 or (x,y) in island_area: # check bounds as well
            return
       
        
        # we must have something that we need to add to the island
        island_area.add((x,y))
        # recursive calls to the rest of the horiz and vert neighbors of this square
        searchIsland(x + 1, y, island_area)
        searchIsland(x - 1, y, island_area)
        searchIsland(x, y + 1, island_area)
        searchIsland(x, y - 1, island_area)

    explored = set()
    for x in range(len(grid2)):
        for y in range(len(grid2[0])):
            if (x, y) not in explored and grid2[x][y] == 1:
                new_island = set()
                searchIsland(x,y, new_island)
                grid2_islands.append(new_island)
                explored.update(new_island)
            
    return len(grid2_islands)

grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
countSubIslands(grid1, grid2)