class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if 1 <= len(s) <= 10**4:
            # Split the string into words and get the last word
            words = s.split()
            if words:
                return len(words[-1])
        return 0
s = input("")
solution = Solution()
print(solution.lengthOfLastWord(s))  # Output: 5