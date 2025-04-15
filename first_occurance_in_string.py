'''
Given two strings needle and haystack, return the index of the first 
occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack) - len(needle) + 1):
            substring = haystack[i:i+len(needle)]
            if substring == needle:
                return i
        return -1