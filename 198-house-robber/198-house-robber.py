class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        memo = [None] * len(nums)
        memo[0] = nums[0]
        memo[1] = nums[1]
        
        for i in range(2, len(nums)):
            if i >= 3:
                memo[i] = max(memo[i-2] + nums[i], memo[i-1], memo[i-3] + nums[i])
            else:
                memo[i] = max(memo[i-2] + nums[i], memo[i-1])
        
        return memo[-1]