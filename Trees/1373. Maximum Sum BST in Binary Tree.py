# Given a binary tree root, return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.


# Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
# Output: 20
# Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        mx = [0]
        def helper(node):
            if not node:
                return [-inf,inf,True,0] #[max,min,is bst or not, current sum]
            left = helper(node.left)
            right = helper(node.right)

            #left and right both should be BST inorder to include root node to BST
            #max of left side should be smaller than root and min of right should be larger than root
            if (left[2] and right[2]) and left[0] < node.val < right[1]:
                #Store the maximum sum
                mx[0] = max(mx[0],node.val+left[3]+right[3])
                return [max(right[0],node.val),min(left[1],node.val),True,node.val+left[3]+right[3]]
            else:
                #IF not BST then it won't contribue to make another BST hence return False
                return [inf,-inf,False,0]
        helper(root)
        return mx[0]