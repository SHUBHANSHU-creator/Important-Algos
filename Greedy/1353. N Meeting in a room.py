# You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and 
# ends at endDayi.

# You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.

# Return the maximum number of events you can attend.


# Input: events = [[1,2],[2,3],[3,4]]
# Output: 3
# Explanation: You can attend all the three events.
# One way to attend them all is as shown.
# Attend the first event on day 1.
# Attend the second event on day 2.
# Attend the third event on day 3.


# Input: events= [[1,2],[2,3],[3,4],[1,2]]
# Output: 4


from ast import List
import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        #mx is the last day of events
        mx = 0
        for s,e in events:
            if e > mx:
                mx = e
        events.sort()
        heap = []
        ind = 0
        res = 0
        for day in range(1,mx+1):
            #check if any event starts on this day
            #if yes then add their ending days
            while ind < n and events[ind][0] == day:
                heapq.heappush(heap,events[ind][1])
                ind += 1
            #if the events dates have expired then remove them since they cannot be attended now
            while heap and heap[0] < day:
                heapq.heappop(heap)
            #if there is some event we can attend today then attend it
            if heap:
                heapq.heappop(heap)
                res +=1
        return res