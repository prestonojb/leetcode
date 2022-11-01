class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countMap = {}
        threshold = math.ceil(len(nums)/2)
        for n in nums:
          countMap[n] = countMap.get(n, 0) + 1
          if countMap[n] >= threshold:
            return n