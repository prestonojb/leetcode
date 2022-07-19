class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_of_arr = sum(nums)
        if sum_of_arr % 2 == 1:
            return False
        
        dp = set()
        dp.add(0)
        target = sum_of_arr // 2

        for i in range(len(nums) -1, -1, -1):
            nextDP = set()
            for t in dp:
                if t + nums[i] == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return target in dp