# Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that 
# for every directed edge u v, vertex u comes before v in the ordering.

#In the given figure
#1 -> 0,
#2 -> 0,
#3 -> 0
#hence possible ordering [3,2,1,0], [2,3,1,0]. In u,v the v should always come after u
#Using BFS
def topoSort( V, adj):
        ans=[]
        
        indegree=[0]*V
        for i in range(V):
            for j in adj[i]:
                indegree[j]+=1
        
        q = []
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
                
        while q:
            node = q.pop(0)
            ans.append(node)
            
            for i in  adj[node]:
                indegree[i]-=1
                if indegree[i] == 0:
                    q.append(i)
                    
        return ans