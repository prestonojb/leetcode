class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        counted = set()
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(r,c):
            if r < 0 or r >= len(grid):
                return
            if c < 0 or c >= len(grid[0]):
                return
            if grid[r][c] == "0":
                return
            if (r,c) in counted:
                return
            
            counted.add((r,c))
            
            for dr, dc in directions:
                row, col = r + dr, c + dc
                dfs(row, col)
                
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in counted:
                    dfs(r, c)
                    res += 1
        
        return res
            