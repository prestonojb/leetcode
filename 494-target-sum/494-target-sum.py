class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(i, _sum):
            if i == len(nums):
                return 1 if _sum == target else 0
            
            if (i, _sum) in cache:
                return cache[(i, _sum)]
            
            cache[(i, _sum)] = dfs(i+1, _sum + nums[i]) + dfs(i+1, _sum - nums[i])
            return cache[(i, _sum)]
        
        return dfs(0, 0)
        