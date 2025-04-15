'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        current_prefix = strs[0]
        for string in strs:
            while not string.startswith(current_prefix):
                current_prefix = current_prefix[:-1]
            if current_prefix == "":
                return ""
        return current_prefix

solution = Solution()            
strs = ["dog","racecar","car"]
# strs = ["flower","flow","flight"]
output = solution.longestCommonPrefix(strs)
print(output)
