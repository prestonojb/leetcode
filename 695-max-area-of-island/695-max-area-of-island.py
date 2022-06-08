class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        curr_area = 0
        res = 0
        
        def dfs(r, c):
            nonlocal res
            nonlocal curr_area
            res = max(curr_area, res)
            if (r < 0 or r >= len(grid)) or (c < 0 or c >= len(grid[0])) or (r,c) in visited:
                return
            visited.add((r,c))
            if grid[r][c]:
                curr_area += 1
                dfs(r-1, c)
                dfs(r+1, c)
                dfs(r, c-1)
                dfs(r, c+1)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visited:
                    curr_area = 0
                    dfs(r, c) # Alter res variable
        
        return res