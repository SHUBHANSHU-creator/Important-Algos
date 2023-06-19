# You are given a 0-indexed integer array nums containing n distinct positive integers. A permutation of nums is called special 
# if:
# For all indexes 0 <= i < n - 1, either nums[i] % nums[i+1] == 0 or nums[i+1] % nums[i] == 0.
# Return the total number of special permutations. As the answer could be large, return it modulo 109 + 7.

 

# Example 1:

# Input: nums = [2,3,6]
# Output: 2
# Explanation: [3,6,2] and [2,6,3] are the two special permutations of nums.
# Example 2:

# Input: nums = [1,4,3]
# Output: 2
# Explanation: [3,1,4] and [4,1,3] are the two special permutations of nums.

# Constraints:

# 2 <= nums.length <= 14
# 1 <= nums[i] <= 109


#Apporach:
#You need to try to make all the permutations yourself, if you are able to add all the elements then add 1 to your ans
#Start with an element and keep track of the last element you added to the permutation so that you verify if the current element can be
#added to the permutation
#Since there will be lot of overlapping intervals you need to cache it
#Constraints are very low hence '''''''''''DP with Bitmasking can be Used''''''''''''''


#DP with Bitmasking
#You create a binary value, since largest value a int can store is 32 bits and long long can store 64 bits hence 
#Bitmasking can only be applied when constraints are low
#So a bit in the binary value tells you if it's been used or not by checking if it's set or not



class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        mod = 1000000007
        al = (1<<n) - 1
        #a number where all bits are set of given length
        #if n ==3: -> al = 1000 - 1 => 111

        @cache
        def per(last,mask):
            #If all numbers are selected or all bits are set, it means you got a permutation
            if mask == al:
                return 1
            total = 0
            for i in range(n):
                #run function on a number who hasn't been included yet and condition satisfies
                if (mask&(1<<i) == 0) and (nums[i]%nums[last] == 0 or nums[last]%nums[i] == 0):
                    total += per(i,mask|(1<<i))
                    #since result can be big hence mod it
                    total%=mod
            return total
        res = 0
        for i in range(n):
            res += per(i,(1<<i))
            res %= mod
        return res
