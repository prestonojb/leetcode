class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf") for _ in range(len(nums))]
        dp[-1] = 0
        
        for i in range(len(nums)-2, -1,-1):
            for k in range(i+1, i + nums[i] + 1):
                if k < len(nums):
                    dp[i] = min(dp[i], 1 + dp[k])
    
        return dp[0]