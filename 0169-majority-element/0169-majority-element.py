class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countMap = {}
        for n in nums:
          countMap[n] = countMap.get(n, 0) + 1
          if countMap[n] >= math.ceil(len(nums)/2):
            return n