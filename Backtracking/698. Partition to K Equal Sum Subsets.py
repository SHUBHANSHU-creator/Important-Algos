# Given an integer array nums and an integer k, return true 
# if it is possible to divide this array into k non-empty subsets whose sums are all equal.


# Input: nums = [4,3,2,3,5,2,1], k = 4
# Output: true
# Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        nums.sort(reverse=True)
        total = sum(nums)
        if total % k != 0:
            return False
        
        target = int(total / k)
        used = [False] * n

        def dfs(index, total, k): 
            if k == 0:
                return True
            if total == 0:
                return dfs(0, target, k - 1)
            for i in range(index, n):
                if i > 0 and not used[i - 1] and nums[i] == nums[i - 1]:
                    continue     
                if used[i] or total - nums[i] < 0:
                    continue
                used[i] = True
                if dfs(i + 1, total - nums[i], k):
                    return True
                used[i] = False
            return False
        
        return dfs(0, target, k)