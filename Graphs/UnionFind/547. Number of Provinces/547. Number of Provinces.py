# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, 
# and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, 
# and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.



from ast import List


class UF:
    def __init__(self,n):
        self.par = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def find(self,x):
        while x != self.par[x]:
            x = self.find(self.par[x])
        return x

    def union(self,n1,n2):
        p1,p2 = self.find(n1),self.find(n2)
        if p1 != p2:
            if self.rank[p2] < self.rank[p1]:
                self.par[p2] = p1
                self.rank[p1] +=1
            else:
                self.par[p1] = p2
                self.rank[p2] +=1

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UF(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    uf.union(i,j)
        p = [uf.find(i) for i in range(n)]
        return len(set(p))
        