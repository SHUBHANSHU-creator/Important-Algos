# Given an integer array nums where every element appears three times except for one, which appears exactly once. 
# Find the single element and return it.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Input: nums = [2,2,3,2]
# Output: 3




class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0

        for i in range(32):
            sm = 0
            for num in nums:
                #handles negative number. we find two's complement to compute a negative number
                if num < 0:
                    num = num & (2**32-1)
                sm += (num >> i) & 1
            #we check the frequncy of the current bit, if its divisible by 3 then it means it was occured in numbers who has frequency=3
            #else the number which occurs once will be having current bit as set bit so store it in ans
            sm %= 3
            ans |= sm << i

        if ans >= 2**31:
            ans -= 2**32

        return ans

        
