class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            n = nums[i]
            if n in d:
                return [d[n], i]
            d[target - n] = i