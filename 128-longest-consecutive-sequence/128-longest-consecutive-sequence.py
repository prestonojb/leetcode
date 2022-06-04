# 1. Sort the string, then count consecutive numbers - O(n log n), O(1)
# 2. Dictionary/Set
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        
        for num in nums:
            if num - 1 not in s:
                length = 1
                while (num+length) in s:
                    length += 1
                res = max(res, length)
        
        return res
                
        