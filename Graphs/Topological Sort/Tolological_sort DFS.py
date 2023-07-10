# Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that 
# for every directed edge u v, vertex u comes before v in the ordering.

#In the given figure
#1 -> 0,
#2 -> 0,
#3 -> 0
#hence possible ordering [3,2,1,0], [2,3,1,0]. In u,v the v should always come after u
#Using BFS

class Solution:
    
    #Function to return list containing vertices in Topological order.
    
    def dfs(self,node, visited, stack, adj):
        visited[node] = True
        for i in adj[node]:
            if visited[i] != True:
                self.dfs(i, visited, stack,adj)
        stack.append(node)
        
    def topoSort(self, V, adj):
        visited = [False]*V
        stack = []
        
        for i in range(V):
            if visited[i] != True:
                self.dfs(i, visited, stack, adj)
        ans = []
        while stack:
            ans.append(stack.pop())
        return ans