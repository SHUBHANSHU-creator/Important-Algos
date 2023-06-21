# A conveyor belt has packages that must be shipped from one port to another within days days.

# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages 
# on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.


# Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
# Output: 15
# Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
# 1st day: 1, 2, 3, 4, 5
# 2nd day: 6, 7
# 3rd day: 8
# 4th day: 9
# 5th day: 10

# Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and 
# splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.


#Solution using Binary Search
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights) , sum(weights)
        #since the largest of weights has to be accomodated hence minimum capacity is min of weights
        #if we try to load all the weights at once then max cap is sum(weights)

        res = r
        #currently keep the cap as r

        #Check if with given capacity we can do the work in given days
        def canShip(cap):
            cur = cap
            ships = 1
            for w in weights:
                if cur - w < 0:
                    ships+=1
                    cur = cap
                cur = cur - w
            return ships <= days

        #binary search over the capacity
        #if current capacity works then try to reduce it else check on right side
        while l<=r:
            cap = (l+r)>>1
            if canShip(cap):
                res = min(res,cap)
                r=cap-1
            else:
                l=cap+1
        return res