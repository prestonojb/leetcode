class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i in range(len(nums)):
            if dict.get(nums[i]):
                return True
            dict[nums[i]] = True
        return False