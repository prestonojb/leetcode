class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        
        def dfs(i, target):
            if i >= len(coins):
                return 0
            if target == 0:
                return 1
            if target < 0:
                return 0
            
            if (i, target) in cache:
                return cache[(i, target)]
            
            cache[(i, target)] = dfs(i, target - coins[i]) + dfs(i+1, target)
            return cache[(i, target)]
        return dfs(0, amount)