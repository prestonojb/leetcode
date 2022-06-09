class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
#         Two pointer appraoch (does not work for height=[5,5,1,7,1,1,5,2,7,6])
#         res = -1
#         l,r = 0, len(heights)-1
        
#         while l <= r:
#             width = r - l + 1
#             height = min(heights[l:r+1])
#             area = width*height
#             res = max(res, area)
#             if heights[l] <= heights[r]:
#                 l += 1
#             else:
#                 r -= 1
        
#         return res
        maxArea = 0
        stack = [] # pair: (index, height)
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))                
        return maxArea
                