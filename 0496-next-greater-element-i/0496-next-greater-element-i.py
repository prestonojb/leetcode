class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
      res = [-1] * len(nums1)
      nums1ValToIdxMap = {}
      
      for i, n in enumerate(nums1):
          nums1ValToIdxMap[n] = i
      
      stack = []
      for n in nums2:        
        while stack and n > stack[-1]:
          val = stack.pop()
          idx = nums1ValToIdxMap[val]
          res[idx] = n
        if n in nums1ValToIdxMap:
          stack.append(n)
      
      return res