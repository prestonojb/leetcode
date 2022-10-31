class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        res = float("inf")
        prefixSum1, prefixSum2 = [0] * n, [0] * n
    
        prefixSum1[0] = grid[0][0]
        prefixSum2[0] = grid[1][0]
        
        for i in range(1, n):
          prefixSum1[i] = prefixSum1[i-1] + grid[0][i]
          prefixSum2[i] += prefixSum2[i-1] + grid[1][i]
        
        for i in range(n):
          top = prefixSum1[-1] - prefixSum1[i]
          bottom = prefixSum2[i-1] if i > 0 else 0
          robot2Score = max(top, bottom)
          res = min(res, robot2Score)
          
        return res