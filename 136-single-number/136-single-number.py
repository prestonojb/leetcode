class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = dict()
        for num in nums:
            if d.get(num):
                del d[num]
            else:
                d[num] = 1
        for key in d.keys():
            return key
        