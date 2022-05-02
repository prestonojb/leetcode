class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {} # {num: index, ...}
        for i in range(len(nums)):
            required = target - nums[i]
            if dict.get(required) is not None:
                return [i, dict.get(required)]
            dict[nums[i]] = i
        