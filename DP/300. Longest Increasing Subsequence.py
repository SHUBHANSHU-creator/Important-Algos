# Given an integer array nums, return the length of the longest strictly increasing 
# subsequence


# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #tabulation
        n = len(nums)
        dp = [1 for i in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],1+dp[j])
        return max(dp)


        #recursion + memoization
        dp = {}
        def dfs(i,last):
            if i == len(nums):
                return 0
            if (i,last) in dp:
                return dp[(i,last)]
            count = 0
            for j in range(i,len(nums)):
                if nums[j] > last:
                    count = max(count,dfs(j,nums[j]))
            dp[(i,last)] = count + 1
            return dp[(i,last)]
        res = 1
        for i in range(len(nums)):
            res = max(res,dfs(i,nums[i]))
        return res