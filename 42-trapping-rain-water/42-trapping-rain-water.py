class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        res = 0
        
        l, r = 0, len(height) - 1 
        leftMax, rightMax = height[l], height[r]
        while l < r:
            if leftMax <= rightMax:
                l += 1
                if min(leftMax, rightMax) - height[l] > 0:
                    res += min(leftMax, rightMax) - height[l]
                leftMax = max(leftMax, height[l])
            else:
                r -= 1
                if min(leftMax, rightMax) - height[r] > 0:
                    res += min(leftMax, rightMax) - height[r]
                rightMax = max(rightMax, height[r])
        return res
        
        