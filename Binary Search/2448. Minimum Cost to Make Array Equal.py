# You are given two 0-indexed arrays nums and cost consisting each of n positive integers.

# You can do the following operation any number of times:

# Increase or decrease any element of the array nums by 1.
# The cost of doing one operation on the ith element is cost[i].

# Return the minimum total cost such that all the elements of the array nums become equal.


# Input: nums = [1,3,5,2], cost = [2,3,1,14]
# Output: 8
# Explanation: We can make all the elements equal to 2 in the following way:
# - Increase the 0th element one time. The cost is 2.
# - Decrease the 1st element one time. The cost is 3.
# - Decrease the 2nd element three times. The cost is 1 + 1 + 1 = 3.
# The total cost is 2 + 3 + 3 = 8.
# It can be shown that we cannot make the array equal with a smaller cost.


#----------Intution
#we want to converge the array to some point where the cost is minimum
#when we want to converge, the median is the point where we get the minimum value



#solition
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def calSum(target):
            res = 0
            for n,c in zip(nums,cost):
                res+= abs(n-target)*c
            return res
        l,r = min(nums),max(nums)
        while l < r:
            mid = (l+r)>>1
            left,right = calSum(mid),calSum(mid+1)
            if left < right:
                r = mid
            else:
                l = mid+1
        return calSum(l)