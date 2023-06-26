# Given two strings text1 and text2, return the length of their longest common subsequence. 
# If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) 
# deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.


# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #Recursion + memoization
        dp = {}
        def dfs(i,j):
            if i == len(text1) or j==len(text2):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            count = dfs(i+1,j)
            count = max(count,dfs(i,j+1))
            if text1[i] == text2[j]:
                count = max(count,1 + dfs(i+1,j+1))
            dp[(i,j)] = count
            return count
        return dfs(0,0)

        #Tabulation
        dp = [[0 for i in range(len(text1)+1)] for j in range(len(text2)+1)]
        for i in range(len(text2)-1,-1,-1):
            for j in range(len(text1)-1,-1,-1):
                if text2[i] == text1[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1],dp[i+1][j])
        return dp[0][0]
            