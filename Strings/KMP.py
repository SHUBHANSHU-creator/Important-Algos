# Given two strings needle and haystack, 
# return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="": return 0
        n = len(haystack)
        m = len(needle)
        lps = [0]*m
        prevLPS, i = 0,1
        while i < m:
            if needle[i] == needle[prevLPS]:
                prevLPS+=1
                lps[i] = prevLPS
                i+=1
            else:
                if prevLPS == 0:
                    lps[i] = 0
                    i+=1
                else:
                    prevLPS = lps[prevLPS-1]
        i = 0
        j = 0
        while i < n and j<m:
            if haystack[i] == needle[j]:
                i+=1
                j+=1
            else:
                if j == 0:
                    i+=1
                else:
                    j = lps[j-1]
            if j==len(needle):
                return i-len(needle)
        return -1