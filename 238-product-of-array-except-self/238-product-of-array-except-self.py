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
        n = len(nums)
        res = [None] * n
        
        # Compute intermediate result
        res[0] = 1
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]
        
        # res = [1,1,2,6]
        postproduct = 1
        for i in range(n-1,-1,-1):
            res[i] *= postproduct
            postproduct *= nums[i]
        
        return res