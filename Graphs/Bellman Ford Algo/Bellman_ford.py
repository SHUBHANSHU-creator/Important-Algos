# Given a weighted, directed and connected graph of V vertices and E edges, Find the shortest distance of all the vertex's 
# from the source vertex S.
# Note: If the Graph contains a negative cycle then return an array consisting of only -1.



class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        #use 1e8 for unreachable nodes
        inf = 10**8
        dist = [inf]*V
        dist[S] = 0
        #It can take upto max v-1 times to use all the edges provided
        for i in range(V-1):
            for u,v,w in edges:
                if dist[u] != inf and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        #made 1 more iteration.
        #Since we should've gotten our min dist array by now but if still gets reduced it means it contains a negative cycle
        for u,v,w in edges:
            if dist[u] != inf and dist[u] + w < dist[v]:
                return [-1]
        return dist