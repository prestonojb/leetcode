class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        res = 0
        def dfs(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return False
            if grid[i][j] == 1:
                return True
            
            grid[i][j] = 1
            
            top = dfs(grid, i, j-1)
            bottom = dfs(grid, i, j+1)
            left = dfs(grid, i-1, j)
            right = dfs(grid, i+1, j)
            
            return top and bottom and left and right
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and dfs(grid, i, j):
                    res += 1
        
        return res
        
