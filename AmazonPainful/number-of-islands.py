import collections
class Solution(object):

    def dfs(self, grid, r,c) : 
        grid[r][c] = "0" #set out current position to 0 so we have already visited
        lst = [(r-1, c), (r+1, c), (r, c-1), (r,c+1)] #array, of places we can search
        for row, col in lst: #for every row and col
            if row >= 0 and col >= 0 and row <len(grid) and col < len(grid[row]) and grid[row][col] == "1": #if we are in bounds, we can call dfs again if we encounter a 1
                self.dfs(grid, row, col)

    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands = 0
        for r in range(len(grid)): #iterate through each element
            for c in range(len(grid[0])): 
                if grid[r][c] == "1": #if we encounter a 1
                    self.dfs(grid, r,c) #call dfs, once dfs is finished we add 1 to the island
                    islands += 1 
        return islands



s = Solution()
print(s.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))