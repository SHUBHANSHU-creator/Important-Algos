class UF:
    def __init__(self,n):
        #par array to find the parent of a node
        self.par = [i for i in range(n)]
        #rank array, used to connect smaller component to larger
        self.rank = [1 for i in range(n)]

    #find fn used to find the parent of a node
    def find(self,x):
        while x != self.par[x]:
            x = self.find(self.par[x])
        return x

    #joining the two nodes
    def union(self,n1,n2):
        p1,p2 = self.find(n1),self.find(n2)
        #If the parent is same that means they are already part of the same component
        #If not then connect the two components
        if p1 != p2:
            #check the larger component using the rank array
            if self.rank[p2] < self.rank[p1]:
                self.par[p2] = p1
                self.rank[p1] +=1
            else:
                self.par[p1] = p2
                self.rank[p2] +=1