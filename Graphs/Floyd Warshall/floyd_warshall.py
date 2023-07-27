# The problem is to find the shortest distances between every pair of vertices in a given edge-weighted directed graph. 
# The graph is represented as an adjacency matrix of size n*n. Matrix[i][j] denotes the weight of the edge from i to j. 
# If Matrix[i][j]=-1, it means there is no edge from i to j.
# Do it in-place.


#In this algo we need to calculate the minimum distance between each and every nodes

class Solution:
	def shortest_distance(self, matrix):
		#in the input the unreachable nodes are marked as -1, we can change it to inf to make code easier
		n = len(matrix)
		inf = float('inf')
		for i in range(n):
			for j in range(n):
				if matrix[i][j] == -1:
					matrix[i][j] = inf
				if i == j:
					matrix[i][j] = 0
		
		#Traverse to all the node starting from all the nodes and try to reach there via every node
		#Take min of current assigned distance and new distance
		for via in range(n):
			for i in range(n):
				for j in range(n):
					matrix[i][j] = min(matrix[i][j], matrix[i][via] + matrix[via][j])
					
		for i in range(n):
			for j in range(n):
				if matrix[i][j] == inf:
					matrix[i][j] = -1
		 