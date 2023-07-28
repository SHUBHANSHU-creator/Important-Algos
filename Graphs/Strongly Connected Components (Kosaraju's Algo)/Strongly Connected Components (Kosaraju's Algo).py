# Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, 
# Find the number of strongly connected components in the graph.


class Solution:
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        stack = []
        visited = set()
        def dfs(node,ad):
            visited.add(node)
            for i in ad[node]:
                if i not in visited:
                    dfs(i,ad)
            stack.append(node)
        
        for i in range(V):
            if i not in visited:
                dfs(i,adj)
                
        adjT = {i:[] for i in range(V)}
        for node in range(V):
            visited.remove(node)
            for nei in adj[node]:
                adjT[nei].append(node)
        
        scc = 0
        while stack:
            node = stack.pop()
            if node not in visited:
                scc +=1
                dfs(node,adjT)
        return scc