# Given an integer array nums, find a 
# subarray
#  that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.


# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #left and right traversal
        n = len(nums)
        mx = -inf
        prod = 1
        for i in range(n):
            prod *= nums[i]
            mx = max(mx,prod)
            if prod == 0:
                prod =1
        prod = 1
        for i in range(n-1,-1,-1):
            prod *= nums[i]
            mx=max(mx,prod)
            if prod == 0:
                prod = 1
        return mx






        #DP
        res = max(nums)
        curMax,curMin = 1,1
        for n in nums:
            if n==0:
                curMax,curMin = 1,1
                continue
            tmp = curMax
            curMax = max(n*curMax,n*curMin,n)
            curMin = min(n*tmp,n*curMin,n)
            res = max(res,curMax)
        return res
                