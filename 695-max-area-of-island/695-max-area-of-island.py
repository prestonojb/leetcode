class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         visited = set()
#         curr_area = 0
#         res = 0
        
#         def dfs(r, c):
#             nonlocal res
#             nonlocal curr_area
#             res = max(curr_area, res)
#             if (r < 0 or r >= len(grid)) or (c < 0 or c >= len(grid[0])) or (r,c) in visited:
#                 return
#             visited.add((r,c))
#             if grid[r][c]:
#                 curr_area += 1
#                 dfs(r-1, c)
#                 dfs(r+1, c)
#                 dfs(r, c-1)
#                 dfs(r, c+1)
        
#         for r in range(len(grid)):
#             for c in range(len(grid[0])):
#                 if (r, c) not in visited:
#                     curr_area = 0
#                     dfs(r, c) # Alter res variable
        
#         return res
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        
        def dfs(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or
                grid[r][c] == 0 or (r, c) in visit):
                return 0
            visit.add((r, c))
            return (1 + dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1))
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        return area