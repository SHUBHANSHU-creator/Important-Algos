# # Given the root of a binary tree, the value of a target node target, and an integer k, 
# # return an array of the values of all nodes that have a distance k from the target node.

# # You can return the answer in any order.

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
# Output: [7,4,1]
# Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.


from collections import deque
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int):
        #First BFS traversal to make the parent Map
        par = {}
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    par[node.left.val] = node
                    q.append(node.left)

                if node.right:
                    par[node.right.val] = node 
                    q.append(node.right)
        #Now the parent Map is ready
        #We are now ready to traverse radially starting from the target node and try to go to a 
        #distance of k
        #Since you need all the nodes at a distance of k, you can use BFS
        q.append(target)
        visited = set()
        cur = 0
        while q:
            if cur == k: break
            cur += 1
            for i in range(len(q)):
                node = q.popleft()
                visited.add(node.val)
                if node.left and node.left.val not in visited:
                    q.append(node.left)
                   
                if node.right and node.right.val not in visited:
                    q.append(node.right)
                    
                if node.val in par and par[node.val].val not in visited:
                    q.append(par[node.val])
                    
        res = []
        while q:
            res.append(q.popleft().val)
        return res