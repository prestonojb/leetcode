# Approach: Precompute products
# nums = [1,2,3,4]
# pre_product = [1,2,6,24]
# post_product = [24,24,12,4]
# res = [pre_product[i-1], post_product[i+1], ...] <- for i in len(nums)
# Time complexity: O(N)


# class Solution:
#     def productExceptSelf(self, nums):
#         n = len(nums)
#         # Compute pre_product
        
#         pre_product = [None] * n
#         j = 1
#         for i in range(n):
#             j *= nums[i]
#             pre_product[i] = j
        
#         # Compute post_product
#         post_product = [None] * n
#         k = 1
#         for i in range(n-1, -1, -1):
#             k *= nums[i]
#             post_product[i] = k
            
#         result = [None] * n
        
#         # Loop to calculate result[i]
#         for i in range(n):
#             pre = pre_product[i-1] if i-1>=0 else 1
#             post = post_product[i+1] if i+1<n else 1
#             result[i] = pre * post
            
#         # Return result
#         return result 

class Solution:
    def productExceptSelf(self, nums):
        # nums = [1,2,3,4]
        n = len(nums)
        res = [None] * n
        
        # Compute intermediate result
        p = 1
        for i in range(n):
            res[i] = p
            p *= nums[i]
        
        p = 1
        for i in range(n-1,-1,-1):
            res[i] *= p
            p *= nums[i]
        
        return res