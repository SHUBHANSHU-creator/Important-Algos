# Given a weighted, undirected and connected graph of V vertices and an adjacency list adj where adj[i] is a list of lists 
# containing two integers where the first integer of each list j denotes there is edge between i and j , 
# second integers corresponds to the weight of that  edge . 
# You are given the source vertex S and You to Find the shortest distance of all the vertex's from the source vertex S. 
# You have to return a list of integers denoting shortest distance between each node and Source vertex S. 


#Input example in the image

import heapq
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    
    def dijkstra(self, V, adj, S):
        #code here

        s=[]
        #we will need a minHeap to fetch the minimum distance present in the array everytime
        heapq.heapify(s)
        ans=[float('inf')]*V
        #add the source to heap with its distance as 0
        #add (distance,prevWeight) to the heap of al the nodes you will reach
        heapq.heappush(s,(0,S))
        ans[S]=0

        while s:
            dist,prev=s.pop()
            for ele,w in adj[prev]:
                w_new=w+dist
                #If you can travel to this node with a shorter path then update the new distance in the ans array
                if w_new<ans[ele]:
                    #add the shortest distance till now and the element so that you can reach other elements with this shorter path
                    heapq.heappush(s,(w_new,ele))
                    ans[ele]=w_new
        return ans